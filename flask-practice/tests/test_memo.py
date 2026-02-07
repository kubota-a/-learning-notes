# tests/test_memo.py
from app import db, Memo


def test_create_memo(logged_in_client, app):
    r = logged_in_client.post(
        "/regist",
        data={"title": "T1", "body": "M1"},  # memo -> body
        follow_redirects=True,
    )
    assert r.status_code == 200

    with app.app_context():
        m = Memo.query.order_by(Memo.id.desc()).first()
        assert m is not None
        assert m.title == "T1"
        assert m.body == "M1"


def test_edit_memo(logged_in_client, app):
    # まず作る
    logged_in_client.post(
        "/regist",
        data={"title": "before", "body": "before memo"},  # memo -> body
        follow_redirects=True,
    )

    with app.app_context():
        m = Memo.query.order_by(Memo.id.desc()).first()
        memo_id = m.id

    # 編集画面GET（表示できること）
    r_get = logged_in_client.get(f"/{memo_id}/edit")
    assert r_get.status_code == 200

    # 更新POST
    r_post = logged_in_client.post(
        f"/{memo_id}/edit",
        data={"title": "after", "body": "after memo"},
        follow_redirects=True,
    )
    assert r_post.status_code == 200

    with app.app_context():
        updated = db.session.get(Memo, memo_id)
        assert updated.title == "after"
        assert updated.body == "after memo"


def test_delete_memo_and_reload_is_safe(logged_in_client, app):
    # まず作る
    logged_in_client.post(
        "/regist",
        data={"title": "del_target", "body": "will delete"},  # memo -> body
        follow_redirects=True,
    )

    with app.app_context():
        m = Memo.query.order_by(Memo.id.desc()).first()
        memo_id = m.id

    # 削除確認ページを GET（= F5相当）
    # ※GET しただけでは削除されないこと
    r_get = logged_in_client.get(f"/{memo_id}/delete")
    assert r_get.status_code == 200

    with app.app_context():
        still_exists = db.session.get(Memo, memo_id)
        assert still_exists is not None

    # 削除を POST
    r_post = logged_in_client.post(
        f"/{memo_id}/delete",
        follow_redirects=True,
    )
    assert r_post.status_code == 200

    with app.app_context():
        deleted = db.session.get(Memo, memo_id)
        assert deleted is None