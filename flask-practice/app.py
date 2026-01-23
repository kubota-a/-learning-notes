from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os  # ファイルパスの扱いに便利

app = Flask(__name__)

# =========================================
# データベース
# =========================================
# プロジェクトフォルダ内にDBを作る設定
basedir = os.path.abspath(os.path.dirname(__file__))    # ベースディレクトリ設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")    # SQLAlchemyの設定
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # パフォーマンストラッキングを無効化 (推奨)

# SQLAlchemyとMigrateのインスタンスを作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DBモデルを定義
class Memo(db.Model):
    __tablename__ = "memo"

    id = db.Column(db.Integer, primary_key=True)    # DBテーブルにid列を設置
    title = db.Column(db.Text, nullable=False)    # DBテーブルにtitle列を設置
    body = db.Column(db.Text, nullable=False)    # DBテーブルにbody列を設置


# ルーティング定義

# トップページ
@app.route("/")    # トップページにアクセスされたら下の関数が動く
def top():
    memo_list = Memo.query.order_by(Memo.id.desc()).all()
    # メモのテーブル(モデル)のDBからデータを取得する準備、idの降順(新しい順)に並べる、全件取得。それをmemo_listに格納
    return render_template('index.html', memo_list=memo_list)    # memo_listを'index.html'に渡して表示させる

# 新規登録画面
@app.route("/regist", methods = ['GET', 'POST'])    # 新規登録画面にアクセスされたら下の関数が動く。GETでもPOSTでも下の関数で処理する。
def regist():
    if request.method == 'POST':    # 今来たリクエストがPOST（登録ボタンが押された）なら、下記の処理を行う
        # フォームから値を取得
        title = request.form.get('title')    # フォームからPOSTされたデータ（request.form）から、name="title" の値を取得して変数titlreに格納
        body = request.form.get('body')    # フォームからPOSTされたデータ（request.form）から、name="body" の値を取得して変数bodyに格納

        # SQLAlchemyでCreate
        memo = Memo(title=title, body=body)
        db.session.add(memo)    # 上記のデータを保存候補に入れる（まだDBに書きこまれてない）
        db.session.commit()    # 保存候補になっていた処理を確定する（DBに書き込みされる）

        # 一覧へ（PRGパターン）
        return redirect("/")    # 登録が終わったら、トップページに戻す（GET）    
    
    # GET（画面を最初に開いたとき）だった場合は画面表示のみ
    return render_template('regist.html')


if __name__ == "__main__":
    app.run(debug=True)
