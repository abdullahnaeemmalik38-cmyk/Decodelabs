from flask import Flask, request, jsonify, render_template
from main import analyze_password
from password_generator import generate_password

app = Flask(__name__)


# -------------------------
# HOME PAGE (UI)
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# SECURITY ANALYSIS PAGE
# -------------------------
@app.route("/analysis")
def analysis_page():
    return render_template("analysis.html")

# -------------------------
# Helper: Input Validation
# -------------------------
def validate_input(data):
    if not data:
        return False, "No JSON body provided"

    if "password" not in data:
        return False, "Missing 'password' field"

    password = data["password"]

    if not isinstance(password, str):
        return False, "Password must be a string"

    if len(password.strip()) == 0:
        return False, "Password cannot be empty"

    return True, password


# -------------------------
# API: Check Password
# -------------------------
@app.route("/check-password", methods=["POST"])
def check_password():
    try:
        data = request.get_json()

        valid, result = validate_input(data)

        if not valid:
            return jsonify({
                "success": False,
                "error": result
            }), 400

        password = result

        analysis = analyze_password(password)

        # -------------------------
        # CLEAN UI RESPONSE FORMAT
        # -------------------------
        return jsonify({
            "success": True,
            "password_length": len(password),
            "result": analysis,
            "ui": {
                "strength": analysis.get("strength"),
                "accepted": analysis.get("accepted"),
                "analysis": analysis.get("analysis", {}),
                "security_metrics": analysis.get("security_metrics", {})
            }
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Internal server error",
            "details": str(e)
        }), 500


# -------------------------
# API: Generate Password
# -------------------------
@app.route("/generate-password", methods=["GET"])
def generate():

    try:
        length = request.args.get("length", default=16, type=int)
        symbols = request.args.get("symbols", default="true").lower() == "true"
        unicode = request.args.get("unicode", default="false").lower() == "true"

        # safety check
        if length < 8:
            return jsonify({
                "success": False,
                "error": "Minimum password length is 8"
            }), 400

        password = generate_password(
            length=length,
            use_symbols=symbols,
            use_unicode=unicode
        )

        return jsonify({
            "success": True,
            "password": password,
            "settings": {
                "length": length,
                "symbols": symbols,
                "unicode": unicode
            }
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Generation failed",
            "details": str(e)
        }), 500


# -------------------------
# HEALTH CHECK (NEW - IMPORTANT FOR DEBUGGING)
# -------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "service": "Password Security API"
    })


# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)