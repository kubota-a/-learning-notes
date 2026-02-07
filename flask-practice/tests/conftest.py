# tests/conftest.py
import os
import sys
import uuid
import pytest

# ✅ pytest 実行時に「プロジェクト直下」を import 対象に入れる（Windowsで特に重要）
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# app.py から FlaskアプリとDB、モデルを読み込む
from app import app as flask_app, db, User, Memo


@pytest.fixture()
def app(tmp_path):
    """
    テスト専用のSQLite DB（ファイル）を毎回作り直す fixture。
    ※ in-memory だと環境によって接続が分かれて事故ることがあるので、ファイルDBにしてる。
    """
    flask_app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{tmp_path / 'test.db'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def unique_userid():
    """毎回かぶらない userid を返す"""
    return f"user_{uuid.uuid4().hex[:10]}"


def signup(client, userid: str, password: str = "pass1234", follow: bool = True):
    return client.post(
        "/signup",
        data={"userid": userid, "password": password},
        follow_redirects=follow,
    )


def login(client, userid: str, password: str = "pass1234", follow: bool = True):
    return client.post(
        "/login",
        data={"userid": userid, "password": password},
        follow_redirects=follow,
    )


@pytest.fixture()
def logged_in_client(client, unique_userid):
    """
    ログイン済みの client を返す。
    ここで作る userid は毎回ユニークだから、テストを何回回しても衝突しない。
    """
    userid = unique_userid
    password = "pass1234"

    signup(client, userid, password, follow=True)
    login(client, userid, password, follow=True)

    return client
