from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    strength = ""

    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)

    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)