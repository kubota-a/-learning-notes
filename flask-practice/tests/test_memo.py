# tests/test_memo.py
from app import db, User

def login(client, userid="taro", password="pw12345"):
    # テスト用ユーザー作成
    # ※useridがユニーク制約なら毎回違う値にしてもOK
    with client.application.app_context():
        user = User(userid=userid)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    # ログイン
    resp = client.post(
        "/login",
        data={"userid": userid, "password": password},
        follow_redirects=False,
    )
    assert resp.status_code == 302


def test_create_memo(client):
    login(client)

    # メモ作成（ここがあなたのフォームnameに依存）
    resp = client.post(
        "/regist",
        data={"title": "test title", "body": "test body"},
        follow_redirects=False,
    )

    # 成功したらトップへリダイレクトされる想定（多い）
    assert resp.status_code in (302, 303)
    location = resp.headers.get("Location", "")
    assert "/" in location
