from argon2 import PasswordHasher

# Configure Argon2id
ph = PasswordHasher()

def hash_password(password: str) -> str:
    """
    Hash a validated password using Argon2id.
    """
    return ph.hash(password)


def verify_password(stored_hash: str, password: str) -> bool:
    """
    Verify a password against its stored Argon2id hash.
    """
    try:
        return ph.verify(stored_hash, password)
    except Exception:
        return False