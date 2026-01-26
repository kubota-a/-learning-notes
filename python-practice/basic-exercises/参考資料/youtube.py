from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
LoginManager,
UserMixin,
login_user,
logout_user,
login_required,
current_user,
)  # 追加
from werkzeug.security import generate_password_hash, check_password_hash  # 追加
import os

# ベースディレクトリ設定 (SQLiteのパス指定に使う)
basedir = os.path.abspath(os.path.dirname(__file__))  # 追加


app = Flask(__name__)

# SQLAlchemyの設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
basedir, "blog.db"
)  # データベースファイルのパスを指定
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
False  # パフォーマンストラッキングを無効化 (推奨)
)

# SQLAlchemyとMigrateのインスタンスを作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Loginの設定
login_manager = LoginManager()  # 追加
login_manager.init_app(app)  # 追加
login_manager.login_view = "login"  # 未ログイン時にリダイレクトするエンドポイント名


# Userモデルの定義
class User(UserMixin, db.Model):  # UserMixinを継承
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
password_hash = db.Column(db.String(255), nullable=False)  # 長めの文字列を想定

def set_password(self, password):
self.password_hash = generate_password_hash(password)

def check_password(self, password):
return check_password_hash(self.password_hash, password)

def __repr__(self):
return f"<User {self.username}>"


# Flask-Loginがユーザー情報をロードするための関数
@login_manager.user_loader
def load_user(user_id):
return User.query.get(int(user_id))


# アプリケーションの secret_key 設定 (flashメッセージやセッション管理に必要)
app.secret_key = "secret"  # 必ず推測されにくい値に変更してください


# ここからデータベースモデルを定義します
class Post(db.Model):
id = db.Column(db.Integer, primary_key=True)  # 記事ID (主キー)
title = db.Column(
db.String(100), nullable=False
)  # タイトル (最大100文字, Null不可)
content = db.Column(db.Text, nullable=False)  # 本文 (長いテキスト, Null不可)
created_at = db.Column(
db.DateTime, server_default=db.func.now()
)  # 作成日時 (デフォルトは現在時刻)

def __repr__(self):
return f"<Post {self.title}>"


# トップページ用のルートを追加
@app.route("/")
def index():
# データベースから記事を全件取得 (作成日時の降順で)
posts = Post.query.order_by(Post.created_at.desc()).all()
# 取得した記事リストをテンプレートに渡す
return render_template("index.html", posts=posts)


# ブログ詳細ページのルート
@app.route("/post/<int:post_id>")
def show_post(post_id):
# IDに対応する記事データをデータベースから取得。見つからなければ404エラー。
post = Post.query.get_or_404(post_id)
# 取得した記事オブジェクトをテンプレートに渡す
return render_template("post.html", post=post)


# 記事管理トップ (一覧表示)
@app.route("/admin")
@login_required  # ログイン必須
def admin_index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    # admin サブフォルダ内の index.html を指定
    return render_template("admin/index.html", posts=posts)


# 記事作成
@app.route("/admin/create", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title or not content:
            flash("タイトルと本文は必須です。", "error")
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            flash("新しい記事が作成されました。", "success")
            return redirect(url_for("admin_index"))  # 管理トップへリダイレクト

    # GETリクエストの場合、またはPOSTでエラーがあった場合
    return render_template("admin/create.html")


# 記事編集
@app.route("/admin/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)  # 編集対象の記事を取得

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]

        if not post.title or not post.content:
            flash("タイトルと本文は必須です。", "error")
        else:
            db.session.commit()  # 変更をコミット
            flash("記事が更新されました。", "success")
            return redirect(url_for("admin_index"))  # 管理トップへリダイレクト

    # GETリクエストの場合、またはPOSTでエラーがあった場合
    # 既存の記事データをフォームに渡して表示
    return render_template("admin/edit.html", post=post)


# 記事削除
@app.route("/admin/delete/<int:post_id>", methods=["POST"])  # POSTのみ許可
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)  # 削除対象の記事を取得
    db.session.delete(post)  # 記事を削除
    db.session.commit()  # 変更をコミット
    flash("記事が削除されました。", "success")
    return redirect(url_for("admin_index"))  # 管理トップへリダイレクト


# ここからログイン・ログアウトのビュー関数を追加
@app.route("/login", methods=["GET", "POST"])
def login():
if current_user.is_authenticated:
return redirect(url_for("index"))  # ログイン済みの場合はトップへ

if request.method == "POST":
username = request.form["username"]
password = request.form["password"]
user = User.query.filter_by(username=username).first()

if user and user.check_password(password):
login_user(user)  # Flask-Loginの機能でログイン
# flash('ログインしました。') # 必要ならflashメッセージ
next_page = request.args.get(
"next"
)  # ログイン後のリダイレクト先があれば取得
return redirect(next_page or url_for("index"))
else:
flash("ユーザー名またはパスワードが正しくありません。")  # エラーメッセージ

return render_template("login.html")


@app.route("/logout")
@login_required  # ログイン必須にするデコレータ
def logout():
logout_user()  # Flask-Loginの機能でログアウト
flash("ログアウトしました。")
return redirect(url_for("index"))


if __name__ == "__main__":
app.run(debug=True)