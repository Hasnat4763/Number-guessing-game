from flask import Flask, render_template, request, session, redirect, url_for
from random import randint

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = randint(1, 100)
        session["attempt"] = 0
    if session["number"] % 2 == 0:
        hint = "This Number is divisible by two"
    else :
        hint = "Try your best"
    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            session["attempt"] += 1
            if guess < session["number"]:
                message = "Too low! Try again."
            elif guess > session["number"]:
                message = "Too high! Try again."
            else:
                message = f"Correct! You guessed it in {session['attempt']} tries."
                session.pop("number")
                session.pop("attempt")
        except ValueError:
            message = "Please enter a valid number."

    return render_template('index.html', message=message , hint = hint)

@app.route("/reset")
def reset():
    session.pop("number", None)
    session.pop("attempt", None)
    return redirect(url_for("index"))