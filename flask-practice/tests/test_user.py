# tests/test_user.py
from app import User, db


def test_user_password_hashing(app):
    with app.app_context():
        u = User(userid="dummy_user")
        u.set_password("secret123")

        assert u.password_hash is not None
        assert u.check_password("secret123") is True
        assert u.check_password("wrong") is False

        db.session.add(u)
        db.session.commit()
