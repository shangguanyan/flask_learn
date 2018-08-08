# Author:zylong
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setting import DbConfig
#这里需要注意，因为没有安装 mysql-python 但是安装了pymql，所以这里连接的时候使用 pymsql
#将配置数据库信息，放到setting 文件中，创建一个class ,DbConfig
#在cmd下 运行这个 from model import * ,db.create_all() 创建表
app = Flask(__name__)
app.config.from_object(DbConfig)
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    username = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32),nullable=False)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            return e
        # finally:
        #     db.session.close()

    def getByNameAndPassword(self):
        getUser = User.query.filter_by(username=self.username,password=self.password).first()
        return getUser

    def getDictUser(self):
        userdict = {"id":self.id,"username":self.username,"password":self.password}
        return userdict

    def getUserName(self):
        return self.username

    @staticmethod
    def getAllUser():
        allUser = User.query.filter_by().all()
        return allUser