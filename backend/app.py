from flask import Flask, render_template, request
from api.register import register_user
from api.login import user_login
from flask_cors import CORS

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

CORS(app)

#endpoints for page rendering
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("landingpage.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/rewardshub")
def rewardshub():
    return render_template("rewardshub.html")


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    return render_template("profile.html", username=username)


@app.route("/transaction", methods =["GET", "POST"])
def transaction():
    return render_template("transactions.html")

#api endpoints

@app.route("/api/login", methods=["POST"])
def api_login():
    return user_login()


@app.route("/api/register", methods=["POST"])
def api_register():
    return register_user()

@app.route("/api/transaction", methods =["POST"])
def api_transaction():
    from api.transaction import transact
    return transact()




if __name__ == "__main__":
    app.run(debug=True)
