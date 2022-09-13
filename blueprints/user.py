from flask import Blueprint, render_template
from flask_mail import Message
from exts import mail

bp = Blueprint("user", __name__, url_prefix='/')


@bp.route("/")
def login():
    return render_template("user_login.html")


@bp.route("/registration")
def regist():
    return render_template("user_regist.html")


@bp.route("/mail")
def mail():
    mess=Message(subject='test',
                 recipients=['350012471@qq.com'],
                 body="email testing")
    mail.send(mess)
    return "sucess"
