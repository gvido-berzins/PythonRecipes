from flask import Blueprint, render_template
from flask_login import current_user, login_required

from . import db

main = Blueprint("main", __name__)


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/admin")
@login_required
def admin():
    name = current_user.name
    username = current_user.username
    return render_template("admin.html", username=username, name=name)
