from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.get("/login")
def login():
    return render_template("login.html")


@auth.post("/login")
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash("Incorrect credentials")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect(url_for("main.admin"))


@auth.post("/signup")
def signup_post():
    json_data = request.get_json()
    username = json_data.get("username")
    name = json_data.get("name")
    password = json_data.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"Status": "Failure"}), 400

    create_new_user(username, name, password)
    return jsonify({"Status": "OK"}), 200


def create_new_user(username, name, password):
    pw_hash = generate_password_hash(password, method="sha256")
    new_user = User(username=username, name=name, password=pw_hash)
    db.session.add(new_user)
    db.session.commit()


@auth.get("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
