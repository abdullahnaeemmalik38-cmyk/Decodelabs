from main import analyze_password

def run_app():

    print("\n🔐 Secure Password Gatekeeper System")
    print("Type 'exit' to quit\n")

    while True:
        password = input("Enter password: ")

        if password.lower() == "exit":
            print("Exiting system...")
            break

        result = analyze_password(password)

        print("\n------------------------")
        print("Strength:", result.get("strength"))
        print("Accepted:", result.get("accepted"))

        if "reason" in result:
            print("Reason:", result["reason"])

        if "analysis" in result:
            print("\n[Pattern Analysis]")
            for k, v in result["analysis"].items():
                print(f"{k}: {v}")

        if "security_metrics" in result:
            print("\n[Entropy]")
            print(result["security_metrics"])

        if "hashed_password" in result:
            print("\n[Secure Hash Generated]")
            print(result["hashed_password"])

        print("------------------------\n")


if __name__ == "__main__":
    run_app()