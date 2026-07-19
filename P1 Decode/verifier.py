from auth import hash_password, verify_password


def demo_verification():
    """
    Simulates storing and verifying a password
    """

    password = "Password123!"

    # Step 1: Hash password (like storing in DB)
    stored_hash = hash_password(password)
    print("Stored Hash:\n", stored_hash)

    # Step 2: Correct password check
    is_valid = verify_password(stored_hash, "Password123!")
    print("\nCorrect Password Check:", is_valid)

    # Step 3: Wrong password check
    is_invalid = verify_password(stored_hash, "WrongPassword")
    print("Wrong Password Check:", is_invalid)


if __name__ == "__main__":
    demo_verification()