import secrets
import string
import random
import unicodedata


# -------------------------
# Unicode pool (safe range)
# -------------------------
UNICODE_POOL = [
    "🔥", "🚀", "⚡", "🔐", "💀", "🧠", "🌐", "🛡️"
]


def generate_password(length=16, use_symbols=True, use_unicode=False):
    """
    Cryptographically secure password generator
    """

    if length < 8:
        raise ValueError("Password length must be at least 8")

    # -------------------------
    # Base character sets
    # -------------------------
    chars = string.ascii_lowercase

    if use_symbols:
        chars += string.ascii_uppercase + string.digits + string.punctuation
    else:
        chars += string.ascii_uppercase + string.digits

    password = []

    # -------------------------
    # Secure random selection
    # -------------------------
    for _ in range(length):
        password.append(secrets.choice(chars))

    # -------------------------
    # Optional Unicode injection
    # -------------------------
    if use_unicode:
        insert_pos = secrets.randbelow(length)
        password[insert_pos] = secrets.choice(UNICODE_POOL)

    return "".join(password)