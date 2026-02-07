# tests/conftest.py
import sys
from pathlib import Path

# プロジェクト直下（app.pyがある場所）を import 対象に追加
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

import pytest
from app import app as flask_app, db


@pytest.fixture()
def app():
    """
    pytest用のFlask app fixture
    - TESTING=True：テストモード
    - DB：SQLiteメモリ（本番DBを汚さない）
    """
    flask_app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY="test-secret",
    )

    with flask_app.app_context():
        db.drop_all()
        db.create_all()

        yield flask_app

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """Flaskのテストクライアント（疑似ブラウザ）"""
    return app.test_client()
