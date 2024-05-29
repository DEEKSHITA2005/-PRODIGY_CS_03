from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


def password_strength_checker(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength_score = 0
    feedback = []

    if length >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if has_upper:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if has_lower:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if has_digit:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if has_special:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "password": password,
        "strength": strength,
        "score": strength_score,
        "feedback": feedback
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    result = password_strength_checker(password)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
