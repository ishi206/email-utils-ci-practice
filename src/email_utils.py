import re


def is_valid_email(email):
    """Return True if the email has a basic valid format."""

    if not isinstance(email, str):
        raise TypeError("email must be a string")

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(pattern, email) is not None


def mask_email(email):
    """Mask part of the email username."""

    if not is_valid_email(email):
        raise ValueError("Invalid email")

    username, domain = email.split("@")

    if len(username) <= 2:
        masked_username = username[0] + "*"
    else:
        masked_username = username[0] + "*" * (len(username) - 2) + username[-1]

    return masked_username + "@" + domain


def has_gmail_domain(email):
    """Return True if email belongs to Gmail."""

    if not is_valid_email(email):
        return False

    return email.lower().endswith("@gmail.com")