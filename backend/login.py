from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

def init_login_routes(app):
    @app.route("/login")
    def login():
        return render_template("login.html")