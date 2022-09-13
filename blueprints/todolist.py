from flask import Blueprint,render_template

bp=Blueprint("todolist",__name__,url_prefix='/list')

@bp.route("/")
def home():
    return render_template("list_home.html")

@bp.route("/detail")
def detail():
    return render_template("list_detail.html")

@bp.route("/add")
def add():
    return render_template("list_add.html")