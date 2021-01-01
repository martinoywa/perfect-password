from flask import Flask, render_template, request

from generator import generate_password, multiple_passwords

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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


if __name__ == "__main__":
    app.run(debug=True)