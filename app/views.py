from flask import Blueprint, render_template, request
from app.generator import generate_password, multiple_passwords


main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        password_length = int(request.form.get("password_length"))
        password_number = int(request.form.get("password_number"))

        if password_number == 1:
            password = generate_password(password_length)
            return render_template("results.html", password=password,
                                   password_number=password_number)
        else:
            password_list = multiple_passwords(password_number,
                                                 password_length)
            return render_template("results.html", password=password_list,
                                   password_number=password_number)
