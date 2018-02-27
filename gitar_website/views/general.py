from flask import Blueprint, render_template
from gitar_website.database import db_session

mod = Blueprint("general", __name__)


@mod.route("/")
def index():
    return render_template("test.html")

