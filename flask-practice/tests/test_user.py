# tests/test_user.py
from app import User


def test_check_password_true_false():
    user = User(userid="testuser")
    user.set_password("abc123")

    assert user.check_password("abc123") is True
    assert user.check_password("wrong") is False
