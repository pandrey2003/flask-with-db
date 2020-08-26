from app.mod_db import session, Members
from flask import flash, redirect, request, url_for
from flask import session as user_session


def check_user(login, password):
    return bool(session.query(Members).filter(Members.login==login, Members.password==password))


def referral():
    url = request.referrer
    user_session["url"] = url
    return user_session["url"]


def signin(login, password):
    if check_user(login, password):
        user_session["logged_in"] = True
        flash("Log in succeeded!", "js")
    else:
        user_session["logged_in"] = False
        flash("Wrong email or password.", "js")


def logout():
    user_session["logged_in"] = False
