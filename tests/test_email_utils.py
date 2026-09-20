import pytest

from src.email_utils import (
    is_valid_email,
    mask_email,
    has_gmail_domain
)


def test_valid_email():

    assert is_valid_email("student@gmail.com") == True


def test_invalid_email():

    assert is_valid_email("student@gmail") == False


def test_email_type():

    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_mask_email():

    email = "student@gmail.com"

    assert mask_email(email) == "s*****t@gmail.com"


def test_gmail_domain():

    assert has_gmail_domain("student@gmail.com") == True
def test_mask_email():
    email = "student@gmail.com"
    assert mask_email(email) == "s*****t@gmail.com"


def test_mask_short_email():
    email = "ab@gmail.com"
    assert mask_email(email) == "a*@gmail.com"


def test_mask_invalid_email():
    with pytest.raises(ValueError):
        mask_email("student@gmail")


def test_gmail_domain_invalid_email():
    assert has_gmail_domain("student@gmail") == False


def test_gmail_domain_case_insensitive():
    assert has_gmail_domain("student@GMAIL.COM") == True


def test_non_gmail_domain():
    assert has_gmail_domain("student@yahoo.com") == False