from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os  # ファイルパスの扱いに便利

app = Flask(__name__)


# データベース

# プロジェクトフォルダ内にDBを作る設定
basedir = os.path.abspath(os.path.dirname(__file__))    # ベースディレクトリ設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")    # SQLAlchemyの設定
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # パフォーマンストラッキングを無効化 (推奨)

# SQLAlchemyとMigrateのインスタンスを作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DBモデルを定義　「memoというテーブルを、Pythonのクラスとして表現します。」
class Memo(db.Model):    # 「このMemoというクラスは、DBのテーブルと対応します」
    __tablename__ = "memo"    # 実際のDB上のテーブル名をmemoに指定

    id = db.Column(db.Integer, primary_key=True)    # 「memoテーブルには、整数型のid列があり、主キーです」
    title = db.Column(db.Text, nullable=False)    # 「memoテーブルには、長めの文字列でnull禁止（必須項目）のtitle列があります」
    body = db.Column(db.Text, nullable=False)    # 「memoテーブルには、長めの文字列でnull禁止（必須項目）のbody列があります」


# ルーティング定義

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
        memo = Memo(title=title, body=body)
        # Memoモデルのtitleカラムに、Python変数titleの値を入れて「memo」というMemoインスタンスを作る・bodyも同様(左：DBのカラム、右：フォームから取得した値を入れたPython変数)
        db.session.add(memo)    # 上記を保存候補に入れる（新規登録の場合必ずaddが必要。まだDBに書きこまれてない）
        db.session.commit()    # 保存候補になっていた処理を確定する（DBに書き込みされる）

        # 一覧へ（PRGパターン）
        return redirect("/")    # 登録が終わったら、トップページに戻す（GET）    
    
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
        return redirect('/')    # 更新が終わったら、トップ画面に戻す（GET）
    
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
        return redirect('/')    # 更新が終わったら、トップ画面に戻す（GET）
    
    # GET（画面を最初に開いたとき）だった場合は編集画面の表示のみ
    return render_template("delete.html", memo=memo)    # 取得したmemoをテンプレートに渡して削除画面を返す


if __name__ == "__main__":
    app.run(debug=True)
