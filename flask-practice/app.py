from flask import Flask, render_template, abort
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

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

# =========================================
# ルート
# =========================================

# トップページのルート
@app.route("/")
def top():
    memo_list = Memo.query.order_by(Memo.id.desc()).all()
    return render_template('index.html', memo_list=memo_list)

if __name__ == "__main__":
    app.run(debug=True)
