import hashlib
import requests


def check_password_pwned(password: str):

    # Step 1: SHA1 hash
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    prefix = sha1[:5]
    suffix = sha1[5:]

    # Step 2: Query HIBP API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)

    if response.status_code != 200:
        return False, "HIBP API error"

    # Step 3: Check returned hashes
    hashes = response.text.splitlines()

    for line in hashes:
        h, count = line.split(':')
        if h == suffix:
            return True, f"Password found in breaches ({count} times)"

    return False, "Password not found in known breaches"