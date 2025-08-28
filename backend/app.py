from flask import Flask, render_template, request
from api.register import register_user
from flask_cors import CORS

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

CORS(app)

# Route for the homepage (login page)
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/rewardshub")
def rewardshub():
    return render_template("rewardshub.html")

@app.route("/api/register", methods=["POST"])
def api_register():
    return register_user()

if __name__ == "__main__":
    app.run(debug=True)
