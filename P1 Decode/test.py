from main import analyze_password

tests = [
    "h55555",
    "abc",
    "password123",
    "Password123!",
    "P@ssw0rd🔥🔥",
    "THISISVERYSTRONG123!@#",
    "1234567",
    "!!!!!!!!!!",
    "你你好你好"
]

for t in tests:
    print("\n========================")
    print("Password:", t)

    result = analyze_password(t)

    # Phase 1 output
    print("Strength:", result.get("strength"))
    print("Accepted:", result.get("accepted"))

    # Phase 1 analysis (pattern detection)
    if "analysis" in result:
        print("\n[Phase 1 Analysis]")
        for k, v in result["analysis"].items():
            print(f"{k}: {v}")

    # Phase 2 output (entropy layer)
    if "security_metrics" in result:
        print("\n[Phase 2 Security Metrics]")
        print("Entropy (bits):", result["security_metrics"]["entropy_bits"])
        print("Estimated crack time (seconds):", result["security_metrics"]["estimated_crack_time_seconds"])

        # Phase 3 output (Gatekeeper reason)
    if "reason" in result:
        print("\n[Phase 3 - Gatekeeper]")
        print("Reason:", result["reason"])

    # Phase 3 output (Argon2id hash)
    if "hashed_password" in result:
        print("\n[Phase 3 - Hash]")
        print(result["hashed_password"])

from password_generator import generate_password

print("Strong password:", generate_password(16))
print("No symbols:", generate_password(16, use_symbols=False))
print("With Unicode:", generate_password(16, use_unicode=True))