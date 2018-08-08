# Author:zylong
from flask import Blueprint
from model import User

user = Blueprint("user",__name__)

@user.route("/<userid>")
def showName(userid):
    u = User.query.filter_by(id=userid).first()
    return u.getUserName()
