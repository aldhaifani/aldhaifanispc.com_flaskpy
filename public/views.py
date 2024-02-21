from flask import Blueprint


views = Blueprint("views", __name__)


@views.route("/")
def favicon():
    return "Hello World"
