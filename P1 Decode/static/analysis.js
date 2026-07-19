const data = JSON.parse(
    localStorage.getItem("analysis")
);

if (!data) {

    window.location.href = "/";
}

document.getElementById("strength").innerText =
    data.strength || "N/A";

document.getElementById("status").innerText =
    data.password_status || "N/A";

document.getElementById("reason").innerText =
    data.reason || "No issues detected.";


// ---------------------
// Analysis
// ---------------------

if (data.analysis) {

    document.getElementById("length").innerText =
        data.analysis.length + " characters";

    const classes = [];

    if (data.analysis.has_lower)
        classes.push("✓ Lowercase Letters");

    if (data.analysis.has_upper)
        classes.push("✓ Uppercase Letters");

    if (data.analysis.has_digit)
        classes.push("✓ Numbers");

    if (data.analysis.has_symbol)
        classes.push("✓ Symbols");

    if (data.analysis.has_unicode)
        classes.push("✓ Unicode Characters");

    document.getElementById("classes").innerHTML =
        classes.map(x => `<li>${x}</li>`).join("");

}


// ---------------------
// Security Metrics
// ---------------------

if (data.security_metrics) {

    document.getElementById("entropy").innerText =
        data.security_metrics.entropy_bits + " bits";

    document.getElementById("crackTime").innerText =
        formatTime(
            data.security_metrics
            .estimated_crack_time_seconds
        );
}


function formatTime(seconds) {

    if (!seconds)
        return "N/A";

    if (seconds > 31536000000)
        return "Billions of Years";

    if (seconds > 31536000)
        return "Years";

    if (seconds > 86400)
        return "Days";

    if (seconds > 3600)
        return "Hours";

    return seconds.toFixed(2) + " Seconds";
}