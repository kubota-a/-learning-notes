# tests/test_auth.py

def test_requires_login_redirect(client):
    resp = client.get("/", follow_redirects=False)

    # 302 = リダイレクト
    assert resp.status_code == 302

    # /login に飛ぶ（next=... が付く）
    location = resp.headers.get("Location", "")
    assert "/login" in location
    assert "next=" in location
