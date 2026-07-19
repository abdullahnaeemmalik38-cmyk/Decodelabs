// Store latest analysis for View Security Analysis page
let latestAnalysis = null;


// ----------------------
// Show / Hide Password
// ----------------------
function togglePassword() {

    const passwordField = document.getElementById("passwordInput");

    passwordField.type =
        passwordField.type === "password"
        ? "text"
        : "password";
}


// ----------------------
// Check Password
// ----------------------
async function checkPassword() {

    const password = document.getElementById("passwordInput").value;

    if (password.trim() === "") {

        alert("Please enter a password.");

        return;
    }

    try {

        const response = await fetch("/check-password", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                password: password
            })

        });

        const data = await response.json();

        if (!data.success) {

            alert("Unable to analyze password.");

            return;
        }

        latestAnalysis = data.result;

        // ----------------------
        // Password Strength
        // ----------------------

        const strengthElement =
            document.getElementById("passwordStrength");

        strengthElement.innerText =
            data.result.strength;

        // ----------------------
        // Reason
        // ----------------------

        document.getElementById("passwordReason").innerText =
            data.result.reason || "No issues detected.";

        if (data.result.strength === "Weak") {

            strengthElement.style.color = "#DC2626";
        }

        else if (data.result.strength === "Medium") {

            strengthElement.style.color = "#F59E0B";
        }

        else if (data.result.strength === "Strong") {

            strengthElement.style.color = "#16A34A";
        }

        else {

            strengthElement.style.color = "#15803D";
        }

        // ----------------------
        // Password Status
        // ----------------------

        document.getElementById("passwordStatus").innerText =
            data.result.password_status;

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to the Flask server.");
    }
}


// ----------------------
// Generate Password
// ----------------------
async function generatePassword() {

    try {

        const response =
            await fetch("/generate-password");

        const data =
            await response.json();

        document.getElementById("generated").innerText =
            data.password;

    }

    catch (error) {

        console.error(error);
    }
}


// ----------------------
// View Security Analysis
// ----------------------
function viewAnalysis() {

    if (!latestAnalysis) {

        alert(
            "Please check a password first."
        );

        return;
    }

    localStorage.setItem(
        "analysis",
        JSON.stringify(latestAnalysis)
    );

    window.location.href =
        "/analysis";
}


// ----------------------
// Enter Key Support
// ----------------------
document
.getElementById("passwordInput")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        checkPassword();
    }

});