from flask import Flask, render_template, request, redirect, abort, flash, url_for, session
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
)
import os

# models.pyからdbとモデルを import
from models import db, User, Memo


# =========================================
# Flaskアプリ本体（直書き）
# =========================================
app = Flask(__name__)

# Render/本番では必ず環境変数で設定する。ローカルは仮でOK。
# session/flash/flask-loginに必要
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


# =========================================
# データベース設定（PostgreSQL想定）
# =========================================
# - Render/Neon では DATABASE_URL が環境変数で渡される前提
# - ローカルでも「Postgres想定で書く」ため、基本は DATABASE_URL を使う運用に寄せる
database_url = os.environ.get("DATABASE_URL")    # 環境変数から"DATABASE_URL"とう値を取得して変数database_urlに格納

if not database_url:    # database_urlがNoneまたは空文字の場合、エラーを出して停止する
    raise RuntimeError("DATABASE_URL is not set")

# サービスによっては "postgres://" が来ることがあるため、接続エラー予防の補正
# （SQLAlchemyは "postgresql://" を推奨）
database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Render本番で接続が安定しやすい設定（なくても動くが、事故が減る）
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True,    # 切れた接続を自動で検知
    "pool_recycle": 300,    # 長時間起動での接続切れ対策
}

# db init（models.pyのdbをアプリに紐付ける）
db.init_app(app)
migrate = Migrate(app, db)


# =========================================
# 認証（ログイン管理）
# =========================================

# --- Flask-Login 設定 ---
login_manager = LoginManager()
login_manager.init_app(app)

# 未ログインで @login_required に入ったとき、"login"に飛ばす
login_manager.login_view = "login"

# flask-login のエラーメッセージ設定　@login_required を付けたページにユーザーがログインなしでアクセスした場合
login_manager.login_message = "ログインが必要です"    # 表示メッセージ
login_manager.login_message_category = "error"    # flashの色（warning/info/errorなど）

# --- ログイン状態の復元 ---
# 「ログイン状態（セッション）から、今ログイン中のUserを復元する仕組み」を登録
@login_manager.user_loader    # デコレータ（関数に役割を付ける）：下記の関数を、flask-loginが「ユーザーIDから今ログイン中のユーザーを復元する係」として使用する
def load_user(user_id: str):    # 上記で「user_loader係」として任命された関数load_userを定義。引数はflask-login から渡されるuser_id（文字列型）
    # user_id →　flask-loginはログイン状態を記憶するとき、内部でユーザーのID（主キー）だけを保存する。辻にリクエストが来たとき、保存してたIDをここに渡してくる
    return db.session.get(User, int(user_id))    # Userテーブルからint型にキャストしたuser_idを検索し、Userインスタンスを取得。そのインスタンスを戻り値として返す


# =========================================
# ✅ADD: 「本番でテーブルが無い」事故を避けるための注意メモ
# =========================================
# Render/Neon では、デプロイ後に必ずDBにテーブルを作る必要がある。
# そのため Flask-Migrate を使って：
#   flask db upgrade
# を実行する（RenderのShell等）。
#
# ※「create_allで自動生成」は、量産では事故りやすいので基本は使わない方針。


# =========================================
# メモ機能（CRUD）
# =========================================

# --- トップページ（メモ一覧） ---
@app.route("/")    # トップページにアクセスされたら下の関数が動く
@login_required    # 未ログインでアクセスされたら"login"に飛ばす
def top():
    memo_list = Memo.query.order_by(Memo.id.desc()).all()
    # メモのテーブル(モデル)のDBからデータを取得する準備、idの降順(新しい順)に並べる、全件取得。それをmemo_listに格納
    return render_template('index.html', memo_list=memo_list)    # memo_listを'index.html'に渡して表示させる

# --- 新規登録 ---
# トップ画面の「新規登録ボタン」からアクセス
@app.route("/regist", methods = ['GET', 'POST'])    # 新規登録画面にアクセスされたら下の関数が動く。GETでもPOSTでも下の関数で処理する。
@login_required    # 未ログインでアクセスされたら"login"に飛ばす
def regist():
    # POST（Create処理）
    if request.method == 'POST':    # 今来たリクエストがPOST（登録ボタンが押された）なら、下記の処理を行う
        # フォームから値を取得　フォームからPOSTされた"title" という名前の値（新規で登録したいメモのタイトル）を取得して、Python変数titlreに格納。bodyも同様
        title = (request.form.get("title") or "").strip()    # ※空白で登録される事故を減らす（サインアップのコメ参照）
        body = (request.form.get("body") or "").strip()

        # 最低限のバリデーション
        # ▼ もしtitleまたはbodyの値が「ちゃんと入ってない」、または、password_rawsの値をstrip()した結果が「ちゃんと入ってない」場合は、
        if not title or not body:    # 詳細はサインアップのコメ参照
            flash("タイトルと本文は必須です。", "error")
            return redirect(url_for("regist"))

        # SQLAlchemyでCreate
        # memoテーブルに入れるための「新しいメモ1件分の箱（Memoオブジェクト）」であるmemoを作成。その箱のtitle欄（カラム）に変数titleの値を入れ、body欄には変数bodyの値を入れておく
        memo = Memo(title=title, body=body)    # ※レコード1行をこれから作る準備
        db.session.add(memo)    # 今作ったmemo（新しいメモ）を、「DBに保存する予定リスト（セッション）」に登録する
        db.session.commit()    # 保存予定リスト（セッション）に入っている変更を、DBに反映して確定する（INSERT実行）
        # 一覧へ（PRGパターン）
        return redirect(url_for("top"))    # 登録が終わったら、トップページに戻す（GET）    
    
    # GET（画面を最初に開いたとき）だった場合は画面表示のみ
    return render_template('regist.html')

# --- 編集 ---　
# トップ画面の「編集ボタン」からアクセス。
@app.route("/<int:id>/edit", methods = ['GET', 'POST'])    # <int:id>にすると自動でintに変換される。「id」はURLパラメータ（どのデータかを指定するための情報）
@login_required    # 未ログインでアクセスされたら"login"に飛ばす
def edit(id):    # URLパラメータが引数。ここで「どのメモを編集するか」が決まる

    # URLでIDを受け取る→DBからその1件を取得→HTML側で初期値入りのフォームを表示（GET/POST共通） 
    memo = db.session.get(Memo, id)    # memoテーブルから主キーがidのレコードを1件取得し、「memo」というオブジェクトとして返す
    if memo is None:    # memoが空だったら=URLに存在しないIDが来たら
        abort(404)    # エラー画面を返す

    # POST（編集ボタンの押下）
    if request.method == 'POST':
        # フォームから値を取得　フォームからPOSTされた"title" という名前の値（新規で登録したいメモのタイトル）を取得して、Python変数titlreに格納。bodyも同様
        title = (request.form.get("title") or "").strip()    # ※空白で登録される事故を減らす（サインアップのコメ参照）
        body = (request.form.get("body") or "").strip()

        # 最低限のバリデーション
        # ▼ もしtitleまたはbodyの値が「ちゃんと入ってない」、または、password_rawsの値をstrip()した結果が「ちゃんと入ってない」場合は、
        if not title or not body:    # 詳細はサインアップのコメ参照
            flash("タイトルと本文は必須です。", "error")
            return redirect(url_for("edit", id=id))

        # Memoクラスから作成したインスタンスmemoのtitleカラムの値を、変数titleの値に書き換える。bodyも同様
        memo.title = title 
        memo.body = body        
        db.session.commit()    # 上記の処理を確定する（）DBに書き込まれる　※すでにDBに存在していたオブジェクトを取得した場合、add()しなくても自動で管理対象になる
        return redirect(url_for("top"))    # 更新が終わったら、トップ画面に戻す（GET）
    
    # GET（画面を最初に開いたとき）だった場合は編集画面の表示のみ
    return render_template("edit.html", memo=memo)    # 取得したmemoをテンプレートに渡して編集画面を返す

# --- 削除 ---
# トップ画面の「削除ボタン」からアクセス。
@app.route("/<int:id>/delete", methods = ['GET', 'POST'])    # <int:id>にすると自動でintに変換される。「id」はURLパラメータ（どのデータかを指定するための情報）
@login_required    # 未ログインでアクセスされたら"login"に飛ばす
def delete(id):    # URLパラメータが引数。ここで「どのメモを削除するか」が決まる

    # URLでIDを受け取る→DBからその1件を取得→（GET/POST共通） 
    memo = db.session.get(Memo, id)    # memoテーブルから主キーがidのレコードを1件取得し、「memo」というオブジェクトとして返す
    if memo is None:    # memoが空だったら=URLに存在しないIDが来たら
        abort(404)    # エラー画面を返す

    # POST（削除ボタンの押下）
    if request.method == 'POST':
        db.session.delete(memo)    # 対象のレコード（オブジェクトmemo）を削除する
        db.session.commit()    # 上記の処理を確定する（）DBに書き込まれる　※すでにDBに存在していたオブジェクトを取得した場合、add()しなくても自動で管理対象になる
        return redirect(url_for("top"))    # 更新が終わったら、トップ画面に戻す（GET）
    
    # GET（画面を最初に開いたとき）だった場合は編集画面の表示のみ
    return render_template("delete.html", memo=memo)    # 取得したmemoをテンプレートに渡して削除画面を返す

# =========================================
# 認証（サインアップ / ログイン / ログアウト）
# =========================================

# --- サインアップ ---
@app.route("/signup", methods=["GET", "POST"])    # ユーザー登録画面にアクセスされたら下記の関数が動く。リクエストはGETとPOSTどちらも受け付ける
def signup():    # signup関数を定義
    if request.method == "POST":    # もしリクエストがPOSTだった場合（フォームの「登録」ボタンが押されたとき）は下記の処理を行う
        # ローカル変数useridに、フォームからPOSTされた"userid"（name属性の辞書キー）に対応する値を取得し、strip()で値の前後の余計なものを削除した状態で格納
        # strip()は、後の入力チェックで「空白だけでユーザーID登録」されてしまうのを防ぐのに大事！
        userid = request.form.get("userid", "").strip()    # get("userid", "")の""はデフォルト値。"userid"というキーがフォームに存在しない場合は空文字を返す
        # ローカル変数password_rawに、フォームからPOSTされた"password"（name属性の辞書キー）に対応する値を取得して格納
        # ユーザーが意図してパスワードに含めた空白スペースを削除してしまわないように、パスワードでは通常strip()は使わない
        password_raw = request.form.get("password", "")    # "password"というキーがフォームに存在しない場合はデフォルト値である空文字を返す

        # 入力チェック（最低限）
        # if not userid　＝　useridの値が「ちゃんと入ってない」なら　→　空文字や空リストやNoneはFalse（偽）扱いになるからこう書く
        # if userid　＝　useridの値が「ちゃんと入っている」なら　→　ちゃんとそれっぽい値が入っているならTrue（真）扱いになるからこう書く
        # ▼ もしuseridの値が「ちゃんと入ってない」、または、password_rawsの値をstrip()した結果が「ちゃんと入ってない」場合は、
        if not userid or not password_raw.strip():
            session["signup_userid"] = userid  # ★入力保持：セッション（ユーザーごとの一時的な保存箱）の中に、辞書としてKey"signup_userid"でuseridの値を保存する
            # ▲ 次のリクエストでも、同じユーザーからのアクセスなら値が保持（ブラウザを閉じるまでページを移動しても保持）され、session["signup_userid"]で値を取り出せる
            flash("ユーザーIDとパスワードを入力してください。", "error")    # 当該flashメッセージ（カテゴリ：error）をflash()でセッションに保存する
            # ※セッションに入れた（予約した）メッセージは、base.html の get_flashed_messages()が拾って次のリクエストで画面に表示させる
            return redirect(url_for("signup"))    # signup関数に紐づいたURL（ユーザー登録画面）にリダイレクトする

        # 入力チェックを通過した変数password_rawの値は、正式にパスワードとして採用することを明示するため変数passwordに格納しなおす（空白を含むパスワードも許可）
        password = password_raw

        # 既存チェック（DBとのつながり）
        # userテーブルの中から【userid（カラム） == 変数useridの値】に一致するレコードを検索して、最初の1件をexistingに格納する
        existing = User.query.filter_by(userid=userid).first()     # ※existingはUserクラスのオブジェクトってことになる
        if existing:    # もしexistingに「値がちゃんと入っている」場合は、（すでに同じuseridを持つユーザーが存在する場合は、）
            session["signup_userid"] = userid  # 入力保持：セッション（ユーザーごとの一時的な保存箱）に、辞書としてキー"signup_userid"でuseridの値を保存する
            # ▲ 次のリクエストでも、同じユーザーからのアクセスなら値が保持（ブラウザを閉じるまでページを移動しても保持）され、session["signup_userid"]で値を取り出せる
            flash("そのユーザーIDはすでに使われています。", "error")    # 当該flashメッセージ（カテゴリ：error）をflash()でセッションに保存する
            # ※セッションに入れた（予約した）メッセージは、base.htmlのget_flashed_messages()が拾って次のリクエストで画面に表示させる
            return redirect(url_for("signup"))    # signup関数に紐づいたURL（ユーザー登録画面）にリダイレクトする

        # （既存レコードと重複がなければ）ユーザー作成
        # userテーブルに入れるための「新しいユーザー1件分の箱（Userオブジェクト）」としてuserを作成。その箱のuserid（カラム）欄に変数useridの値をセットする
        user = User(userid=userid)    # ※レコード1行をこれから作る準備をしている段階
        user.set_password(password)    # 変数passwordの値）を、set_password()でハッシュ化して箱（user）のpassword欄にセットする
        db.session.add(user)    # 上記で作ったuser（新規ユーザー）を、「DBに保存する予定リスト（セッション）」に登録する　session→DB操作の一時置き場/まとめて管理する箱
        db.session.commit()    # 保存予定リスト（セッション）に入っている変更を確定してDBに書き込む（INSERTを実行）

        # 登録成功時は削除：セッションから"signup_userid"というキーを削除してそのキーの値を返す（実際には戻り値は使わない）。もしキーがなくてもエラーにしないためNoneを返す
        session.pop("signup_userid", None)  
        flash("ユーザー登録が完了しました。ログインしてください。", "success")    # 当該メッセージ（カテゴリ：success）をflash()でセッションに保存する
        # ※セッションに入れたメッセージは、base.htmlのget_flashed_messages()が拾って次のリクエストで画面に表示させる
        return redirect(url_for("login"))    # login関数に紐づいたURL（ログイン画面）にリダイレクトする

    # GET（画面を最初に開いたときだった場合はユーザー登録画面の表示のみ・前回POSTで失敗していた場合には、その時に保存したuseridを復元
    # セッションからキー"signup_userid"の値を取り出して削除する。取り出した値を変数useridに格納（HTMLが拾って返す）。キーが存在しなければ空文字を返す。
    userid = session.pop("signup_userid", "")     # ▲ POST失敗後なら保存された文字列が、そうでなけれが空文字がHTMLのuseridに渡されることになる
    return render_template("signup.html", userid=userid)

# --- ログイン ---
# ※ユーザー登録画面と共通のコードには■
@app.route("/login", methods=["GET", "POST"])    # "/login"にアクセスされたら、下の関数で処理。GET（画面表示）とPOST（フォーム送信）どちらも受け付ける
def login():    # ログイン画面の表示とログイン処理を担当する関数を定義
    if request.method == "POST":    # ■もし今のリクエストがPOST（＝フォーム送信された）なら、ログイン処理をする
        # ■フォームから取り出したuseridを、前後の空白を削除した状態で変数useridに格納。useridというキーが存在しない場合は空文字にする
        userid = request.form.get("userid", "").strip()    # ▲ ユーザーがうっかり前後にスペースを入れてもログインできるようにする（"akina " を "akina" とみなす）
        # ■フォームから取り出したpasswordを、加工なしで変数password_rawに格納。passwordというキーが存在しなければ空文字にする
        password_raw = request.form.get("password", "")    # ▲ PWは「空白も含めて入力されたもの」が重要なので、とりあえず生のまま受け取る

        # 入力チェック（最低限）
        # ■もしuseridに値が「ちゃんと入ってない」、または、password_rawの値をstrip()したものが「ちゃんと入ってない」なら、
        if not userid or not password_raw.strip():    # ■もしuseridが空（＝未入力）、またはpassword_rawが空白だけで実質空（＝strip()した値が空になった）なら、
            session["login_userid"] = userid    # ■★入力保持：セッションの中に、辞書としてキー"login_userid"のバリューをuseridの値で保存する
            # ▲ ■次のリクエストでも、同じユーザーからのアクセスなら値が保持（ブラウザを閉じるまでページを移動しても保持）され、session["login_userid"]で値を取り出せる
            flash("ユーザーIDとパスワードを入力してください。", "error")    # ■当該メッセージ（カテゴリ：エラー）をflash()でセッションに保存する
            # ■セッションに入れたメッセージは、base.htmlのget_flashed_messages()が拾って次のリクエストで「1回だけ」画面に表示させる
            return redirect(url_for("login"))    # ■login関数に紐づいたURL（ログイン画面）にリダイレクトして処理を終える
        
        # ■入力チェックを通過したpassword_rawの値は、正式にパスワードとして扱うことを明示するため変数passwordに格納しなおす
        password = password_raw  # ■パスワードは空白を含めてOK（意図した空白を消さない）

        # userテーブルの中から、userid（カラム）が変数useridの値に一致するレコードを検索して、最初の1件を取り出して変数userに格納。一致するものがなければNoneを返す
        user = User.query.filter_by(userid=userid).first()    # ※userはUserクラスのインスタンス、オブジェクトとなる

        # ログイン失敗
        # もし変数userの値がNone（一致するIDがない）またはUserメソッドcheck_password()によるPW照合の結果が「trueじゃない＝false」（PWが一致しない）場合は、
        if user is None or not user.check_password(password):
            session["login_userid"] = userid    # 入力保持：セッションに、辞書としてキー"login_userid"でuseridの値を保存する
            flash("ユーザーIDまたはパスワードが違います。", "error")    # 当該メッセージ（カテゴリ：error）をセッションに保存する　※ユーザー列挙対策としてエラーメッセージは統一
            # ▲ ※セッションに入れたメッセージは、base.htmlのget_flashed_messages()が拾って1度だけ次のリクエストで画面に表示される
            return redirect(url_for("login"))    # login関数に紐づいたURLにリダイレクトして処理を終了（二重送信防止&flash表示のため）

        # ログイン成功
        login_user(user)    # このユーザーを「ログイン状態」として記録する（flask_loginのツール関数）
        # （入力復元用に）保存していたlogin_useridというキーを削除してそのキーの値を返す（実際には戻り値は使わない）。もしキーがなくてもエラーにしないためNoneを返す
        session.pop("login_userid", None)
        flash("ログインしました。", "success")    # 当該メッセージ（カテゴリ：success）をセッションに保存
        # ▲ ※セッションに入れたメッセージは、base.htmlのget_flashed_messages()が拾って1度だけ次のリクエストで画面に表示される

        # もしログイン前にアクセスしようとしていたページがあるなら、そこへ戻す（ログイン画面は「踏み台」になることが多いので、元の目的地へ戻すのが親切）
        # GETのURLクエリ（?xxx=yyy）をまとめた辞書（request.args）から、キー"next"の値（＝元のURL）を取り出してnext_urlに格納。URLに「next=〇〇」がついてなければNone
        next_url = request.args.get("next")
        return redirect(next_url or url_for("top"))    # next_urlにちゃんと値が入っていればnext_urlにリダイレクト、そうでなければtop関数に紐づいたURLへリダイレクト

    # GET：前回失敗した userid を復元
    # ログイン失敗時にセッションに保存していたlogin_useridというキーを削除してそのキーの値（キーがなかったら空文字）を変数useridに格納
    userid = session.pop("login_userid", "")    # ▲ Noneだとフォーム側で表示が変になるかもだから、値がないときは空文字のほうが安全
    return render_template("login.html", userid=userid)    # login.htmlを表示してテンプレートに変数useridの値を渡す（入力復元用）

# --- ログアウト ---
@app.route("/logout", methods=["POST"])    # /logoutにアクセスされたら下の関数で処理。リクエストはPOSTのみ受け付ける　※ログアウトはCSRF対策のためPOSTにする
@login_required    # ログインしていない状態で /logout を勝手に叩かれるとセッションの扱いが不明確になって攻撃される可能性あり（Flask-Login の公式ドキュメントでも推奨）
def logout():    # ログアウト関数を定義
    logout_user()    # flask_loginのツール関数logout_user()を実行（ログイン状態を保持していた「セッション中のユーザー情報」を削除する）
    flash("ログアウトしました。", "success")    # セッションに当該メッセージ（カテゴリはsuccess）を一時保存し、次のリクエストで表示できるように準備
    return redirect(url_for("top"))    # top関数に紐づくよう生成されたURLにリダイレクトして処理を終了
    # POSTで受けて、処理が終わったら安全な場所（トップページ）にGETでリダイレクトして終了！→PRGパターン（Post/Redirect/Get）


# =========================================
# ✅ADD: Render/本番起動の前提（uv運用のメモ）
# =========================================
# ローカルでの実行例（uv）:
#   uv run flask --app app run --debug
# or
#   uv run python app.py
#
# Render本番は gunicorn を使う（例）:
#   gunicorn app:app


# =========================================
# アプリ起動
# =========================================
if __name__ == "__main__":
    app.run(debug=True)
