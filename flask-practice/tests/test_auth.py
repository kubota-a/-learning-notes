# tests/test_memo.py
from app import Memo, db


def test_create_memo(logged_in_client, app):
    res = logged_in_client.post(
        "/regist",
        data={"title": "t1", "body": "b1"},
        follow_redirects=True,
    )
    assert res.status_code == 200

    with app.app_context():
        memo = Memo.query.filter_by(title="t1").first()
        assert memo is not None
        assert memo.body == "b1"


def test_edit_memo(logged_in_client, app):
    with app.app_context():
        memo = Memo(title="before", body="body")
        db.session.add(memo)
        db.session.commit()
        memo_id = memo.id

    res = logged_in_client.post(
        f"/{memo_id}/edit",
        data={"title": "after", "body": "body2"},
        follow_redirects=True,
    )
    assert res.status_code == 200

    with app.app_context():
        updated = db.session.get(Memo, memo_id)
        assert updated.title == "after"
        assert updated.body == "body2"


def test_delete_memo(logged_in_client, app):
    with app.app_context():
        memo = Memo(title="del", body="delbody")
        db.session.add(memo)
        db.session.commit()
        memo_id = memo.id

    res = logged_in_client.post(
        f"/{memo_id}/delete",
        follow_redirects=True,
    )
    assert res.status_code == 200

    with app.app_context():
        deleted = db.session.get(Memo, memo_id)
        assert deleted is None
