# entropy.py
import math

ASCII_SPACE = 95
UNICODE_SPACE = 143000


def calculate_search_space(password: str, has_unicode: bool):
    """
    Estimate character pool size
    """

    if has_unicode:
        return UNICODE_SPACE
    return ASCII_SPACE


def calculate_entropy(password: str, has_unicode: bool):
    """
    Entropy = length × log2(search_space)
    """

    length = len(password)
    pool = calculate_search_space(password, has_unicode)

    entropy = length * math.log2(pool)

    return round(entropy, 2)


def estimate_crack_time(entropy_bits: float, guesses_per_sec=1e9):
    """
    Rough brute-force time estimation
    (modern GPU scale)
    """

    total_combinations = 2 ** entropy_bits
    seconds = total_combinations / guesses_per_sec

    return seconds