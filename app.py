from flask import Flask,request,url_for,render_template,redirect
from model import *
from wtforms import Form,StringField,PasswordField,validators

from flask_restful import Api

app = Flask(__name__)

api = Api(app)
from userapi import *
api.add_resource(Authentication,"/auth")
from user import *
app.register_blueprint(user,url_prefix = "/user")

class LoginForm(Form):
    username = StringField("username",[validators.required])
    password = PasswordField("password",[validators.required])

@app.route("/register",methods=["GET","POST"])
def register():
    allUser = User.getAllUser()
    myform = LoginForm(request.form)
    if "POST" == request.method:
        u = User(myform.username.data,myform.password.data)
        u.add()
        return redirect(url_for("register"))
    return render_template("register.html", form=myform, users = allUser)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/user/<id>")
def getUser(id):
    return "hello user id:"+id

@app.route("/users")
def getUserRequest():
    id = request.args.get("id")
    return "hello getUserRequest id:"+id

@app.route("/query_url",methods=["POST"])
def query_url():
    query_url = url_for("getUserRequest")
    return "getUrl :"+query_url

@app.route("/myfirst")
def myfirst():
    content = "this is first flask"
    return render_template("index.html", content=content)


if __name__ == '__main__':
    app.run()
