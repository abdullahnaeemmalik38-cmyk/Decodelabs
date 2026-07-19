from validator import check_password_strength
from entropy import calculate_entropy, estimate_crack_time
from auth import hash_password


def analyze_password(password: str):

    # -----------------------
    # Phase 1 - Validation
    # -----------------------
    result = check_password_strength(password)

    # -----------------------
    # Rejected Passwords
    # -----------------------
    if not result["accepted"]:

        result["password_status"] = (
            "❌ Password is rejected for entropy calculation and secure hashing."
        )

        return result

    # -----------------------
    # Phase 2 - Entropy
    # -----------------------
    has_unicode = result["analysis"]["has_unicode"]

    entropy = calculate_entropy(
        password,
        has_unicode
    )

    crack_time = estimate_crack_time(
        entropy
    )

    result["security_metrics"] = {
        "entropy_bits": round(entropy, 2),
        "estimated_crack_time_seconds": crack_time
    }

    # -----------------------
    # Strength Refinement
    # -----------------------
    if entropy < 40:

        result["strength"] = "Weak"

    elif entropy < 70:

        result["strength"] = "Medium"

    elif entropy < 100:

        result["strength"] = "Strong"

    else:

        result["strength"] = "Very Strong"

    # -----------------------
    # Gatekeeper Rule
    # -----------------------
    if result["strength"] == "Weak":

        result["accepted"] = False

        result["reason"] = (
            "Password rejected by Gatekeeper."
        )

        result["password_status"] = (
            "❌ Password is rejected for entropy calculation and secure hashing."
        )

        return result

    # -----------------------
    # Phase 3 - Argon2id
    # -----------------------
    result["hashed_password"] = (
        hash_password(password)
    )

    result["password_status"] = (
        "✅ Password is accepted for entropy calculation and secure hashing."
    )

    return result


# Quick Test
if __name__ == "__main__":

    pwd = input("Enter password: ")

    print(
        analyze_password(pwd)
    )