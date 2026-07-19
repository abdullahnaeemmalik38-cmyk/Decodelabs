# validator.py
from hibp_check import check_password_pwned
import unicodedata
import string

# -------------------------
# Phase 3.5 Security Lists
# -------------------------
COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome"
}

COMMON_PATTERNS = [
    "123", "321", "111", "000", "abc", "qwerty"
]

SEQUENTIALS = [
    "012", "123", "234", "345", "456", "567", "678", "789"
]


# -------------------------
# Weak Pattern Detector
# -------------------------
def detect_weak_patterns(password: str):

    lower = password.lower()

    # 1. Blacklist check
    if lower in COMMON_PASSWORDS:
        return True, "Blacklisted common password"

    # 2. Pattern check
    for p in COMMON_PATTERNS:
        if p in lower:
            return True, f"Weak pattern detected: {p}"

    # 3. Sequential numbers check
    for seq in SEQUENTIALS:
        if seq in password:
            return True, "Sequential number pattern detected"

    return False, None


# -------------------------
# Main Validator
# -------------------------
def check_password_strength(password: str):
    """
    Phase 1 + Phase 3.5:
    - Structure validation
    - Pattern detection
    - O(n) scan
    """

    # -------------------------
    # Gatekeeper Rule (CRITICAL)
    # -------------------------
    if len(password) < 8:
        return {
            "strength": "Weak",
            "reason": "Password too short (< 8 characters)",
            "accepted": False
        }
    # -------------------------
    # BREACH CHECK (HIBP)
    # -------------------------
    is_pwned, reason = check_password_pwned(password)

    if is_pwned:
        return {
        "strength": "Weak",
        "accepted": False,
        "reason": reason
    }
    # -------------------------
    # NEW: Weak pattern check (BEFORE analysis)
    # -------------------------
    is_weak, reason = detect_weak_patterns(password)

    if is_weak:
        return {
            "strength": "Weak",
            "reason": reason,
            "accepted": False
        }

    # -------------------------
    # Flags
    # -------------------------
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    has_unicode = False

    # -------------------------
    # Single Pass Scan (O(n))
    # -------------------------
    for char in password:

        if ord(char) > 127:
            has_unicode = True

        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True
        else:
            category = unicodedata.category(char)
            if category.startswith("S") or category.startswith("P"):
                has_symbol = True

    # -------------------------
    # Strength Calculation
    # -------------------------
    categories = sum([
        has_lower,
        has_upper,
        has_digit,
        has_symbol
    ])

    # -------------------------
    # Strength Rules
    # -------------------------
    if categories <= 2:
        strength = "Weak"
    elif categories == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    if len(password) >= 12 and categories == 4:
        strength = "Very Strong"

    # -------------------------
    # Output
    # -------------------------
    return {
        "strength": strength,
        "accepted": True,
        "analysis": {
            "length": len(password),
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_symbol": has_symbol,
            "has_unicode": has_unicode,
            "categories_used": categories
        }
    }