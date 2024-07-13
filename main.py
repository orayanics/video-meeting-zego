from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secrets"

@app.route("/")
def home():
    return redirect(url_for("join"))

@app.route("/meeting")
def meeting():
    username = request.args.get('username', 'Guest')
    return render_template("meeting.html", username=username)


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        room_id = request.form.get("roomID")
        # Generate a random username
        random_username = "User" + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return redirect(url_for("meeting", roomID=room_id, username=random_username))

    return render_template("join.html")

if __name__ == "__main__":
    app.run(debug=True)
