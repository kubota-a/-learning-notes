from flask import Flask, render_template, request, redirect, abort, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash    # Flaskの下地になっているwerkzeug（ワークツォイク）ライブラリの関数をインポート
import os


# =========================================
# Flaskアプリ本体
# =========================================
app = Flask(__name__)

# ■セッション/flash/flask-loginに必要（本番では必ず環境変数で設定）
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


# =========================================
# データベース設定（SQLAlchemy / Migrate）
# =========================================
# プロジェクトフォルダ内にDBを作る設定
basedir = os.path.abspath(os.path.dirname(__file__))    # ベースディレクトリ設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")    # SQLAlchemyの設定
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # パフォーマンストラッキングを無効化 (推奨)

# SQLAlchemyとMigrateのインスタンスを作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# =========================================
# ■Flask-Login 設定（ログイン管理）
# =========================================
login_manager = LoginManager()
login_manager.init_app(app)

# 未ログインで @login_required に入ったとき、"login"に飛ばす
login_manager.login_view = "login"

# flask-login のエラーメッセージ設定　@login_required を付けたページにユーザーがログインなしでアクセスした場合
# login_manager.login_message = "ログインが必要です。"    # 表示メッセージ
# login_manager.login_message_category = "warning"    # flashの色（warning/info/errorなど）


# =========================================
# DBモデル
# =========================================

# ■ユーザー　「userというテーブルを、Pythonのクラスとして表現します」
class User(UserMixin, db.Model):    # このUserというクラスは、DBのテーブルと対応します
    __tablename__ = "user"    # 実際のDB上のテーブル名をuserに指定

    id = db.Column(db.Integer, primary_key=True)    # 整数型で主キーのカラム
    userid = db.Column(db.String(80), unique=True, nullable=False)    # 80文字以内の文字列型で、値の重複を許さない、null禁止（必須項目）
    password_hash = db.Column(db.String(255), nullable=False)    # 255文字以内の文字列型で、null禁止（必須項目）※平文で保存せずハッシュ化

    # Userクラス専用の、パスワードをハッシュ化するメソッド　signup（ユーザー作成）のときに使用
    # Userクラスのメソッドset_passwordを定義。引数はUserインスタンス自身、パスワード（文字列型）。戻り値の型ヒント（アノテーション）：戻り値なし（noneを返す）
    def set_password(self, password: str) -> None:
        # ツール関数generate_password_hashに、ユーザーが入力した平文のパスワードを渡してハッシュ化した文字列をself.password_hash（DBカラム）に保存する
        self.password_hash = generate_password_hash(password)

    # パスワードを照合するメソッド　login（ログイン）のときに使用
    # Userクラスのメソッドcheck_passwordを定義。引数はUserインスタンス自身、パスワード（文字列型）。戻り値の型ヒント：bool型
    def check_password(self, password: str) -> bool:
        # ツール関数check_password_hashに、DBに保存されているハッシュ化されたパスワードと、ユーザーが入力した平文のパスワードを渡して照合した結果を返す（true/false）
        return check_password_hash(self.password_hash, password)

    # デバッグ、Flaskシェル、ログ出力した際に、オブジェクトを「User 3」のように短くわかりやすく表すための関数
    def __repr__(self) -> str:
        return f"<User {self.userid}>"

# 「ログイン状態（セッション）から、今ログイン中のUserを復元する仕組み」を登録
@login_manager.user_loader    # デコレータ（関数に役割を付ける）：下記の関数を、flask-loginが「ユーザーIDから今ログイン中のユーザーを復元する係」として使用する
def load_user(user_id: str):    # 上記で「user_loader係」として任命された関数load_userを定義。引数はflask-login から渡されるuser_id（文字列型）
    # user_id →　flask-loginはログイン状態を記憶するとき、内部でユーザーのID（主キー）だけを保存する。辻にリクエストが来たとき、保存してたIDをここに渡してくる
    return User.query.get(int(user_id))    # Userテーブルからint型にキャストしたuser_idを検索し、Userインスタンスを取得。そのインスタンスを戻り値として返す


# メモ　「memoというテーブルを、Pythonのクラスとして表現します。」
class Memo(db.Model):    # 「このMemoというクラスは、DBのテーブルと対応します」
    __tablename__ = "memo"    # 実際のDB上のテーブル名をmemoに指定

    id = db.Column(db.Integer, primary_key=True)    # 「memoテーブルには、整数型のid列があり、主キーです」
    title = db.Column(db.Text, nullable=False)    # 「memoテーブルには、長めの文字列でnull禁止（必須項目）のtitle列があります」
    body = db.Column(db.Text, nullable=False)    # 「memoテーブルには、長めの文字列でnull禁止（必須項目）のbody列があります」

    # デバッグ、Flaskシェル、ログ出力した際に、オブジェクトを「Memo 3」のように短くわかりやすく表すための関数
    def __repr__(self) -> str:
        return f"<Memo {self.id}>"


# =========================================
# ルーティング（メモCRUD）
# =========================================
# トップページ
@app.route("/")    # トップページにアクセスされたら下の関数が動く
def top():
    memo_list = Memo.query.order_by(Memo.id.desc()).all()
    # メモのテーブル(モデル)のDBからデータを取得する準備、idの降順(新しい順)に並べる、全件取得。それをmemo_listに格納
    return render_template('index.html', memo_list=memo_list)    # memo_listを'index.html'に渡して表示させる

# 新規登録画面　トップ画面の「新規登録ボタン」からアクセス
@app.route("/regist", methods = ['GET', 'POST'])    # 新規登録画面にアクセスされたら下の関数が動く。GETでもPOSTでも下の関数で処理する。
def regist():
    # POST（Create処理）
    if request.method == 'POST':    # 今来たリクエストがPOST（登録ボタンが押された）なら、下記の処理を行う
        # フォームから値を取得　フォームからPOSTされた"title" という名前の値（新規で登録したいメモのタイトル）を取得して、Python変数titlreに格納。bodyも同様
        title = request.form.get('title')
        body = request.form.get('body')

        # SQLAlchemyでCreate
        # memoテーブルに入れるための「新しいメモ1件分の箱（Memoオブジェクト）」であるmemoを作成。その箱のtitle欄（カラム）に変数titleの値を入れ、body欄には変数bodyの値を入れておく
        memo = Memo(title=title, body=body)    # ※レコード1行をこれから作る準備
        db.session.add(memo)    # 今作ったmemo（新しいメモ）を、「DBに保存する予定リスト（セッション）」に登録する
        db.session.commit()    # 保存予定リスト（セッション）に入っている変更を、DBに反映して確定する（INSERT実行）

        # 一覧へ（PRGパターン）
        return redirect(url_for("top"))    # 登録が終わったら、トップページに戻す（GET）    
    
    # GET（画面を最初に開いたとき）だった場合は画面表示のみ
    return render_template('regist.html')

# 編集画面　トップ画面の「編集ボタン」からアクセス。
@app.route("/<int:id>/edit", methods = ['GET', 'POST'])    # <int:id>にすると自動でintに変換される。「id」はURLパラメータ（どのデータかを指定するための情報）
def edit(id):    # URLパラメータが引数。ここで「どのメモを編集するか」が決まる

    # URLでIDを受け取る→DBからその1件を取得→HTML側で初期値入りのフォームを表示（GET/POST共通） 
    memo = Memo.query.get(id)    # memoテーブルから主キーがidのレコードを1件取得し、「memo」というオブジェクトとして返す
    if memo is None:    # memoが空だったら=URLに存在しないIDが来たら
        abort(404)    # エラー画面を返す

    # POST（編集ボタンの押下）
    if request.method == 'POST':
        # Memoクラスから作成したインスタンスmemoのtitleカラムの値を、フォームからPOSTされた"title" という名前の値（メモの新しいタイトル）に書き換える。bodyも同様
        memo.title = request.form.get('title')
        memo.body = request.form.get('body')

        db.session.commit()    # 上記の処理を確定する（）DBに書き込まれる　※すでにDBに存在していたオブジェクトを取得した場合、add()しなくても自動で管理対象になる
        return redirect(url_for("top"))    # 更新が終わったら、トップ画面に戻す（GET）
    
    # GET（画面を最初に開いたとき）だった場合は編集画面の表示のみ
    return render_template("edit.html", memo=memo)    # 取得したmemoをテンプレートに渡して編集画面を返す

# 削除画面　トップ画面の「削除ボタン」からアクセス。
@app.route("/<int:id>/delete", methods = ['GET', 'POST'])    # <int:id>にすると自動でintに変換される。「id」はURLパラメータ（どのデータかを指定するための情報）
def delete(id):    # URLパラメータが引数。ここで「どのメモを削除するか」が決まる

    # URLでIDを受け取る→DBからその1件を取得→（GET/POST共通） 
    memo = Memo.query.get(id)    # memoテーブルから主キーがidのレコードを1件取得し、「memo」というオブジェクトとして返す
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
# ユーザー登録画面
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

# ユーザー登録画面の確認用
@app.route("/login", methods=["GET", "POST"])
def login():
    return "login page (未実装)"





if __name__ == "__main__":
    app.run(debug=True)
