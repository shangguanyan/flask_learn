# Author:zylong
from flask_restful import reqparse,Resource
from model import User
import json
auth = reqparse.RequestParser()

class Authentication(Resource):
    def get(self):
        pass
    def post(self):
        auth.add_argument("username",required=True,help="name is required")
        auth.add_argument("password",required=True,help="密码是必输的")
        args = auth.parse_args()
        username = args["username"]
        password = args["password"]
        u = User(username,password)
        getUser = u.getByNameAndPassword()
        if u is not None :
            temp = getUser.getDictUser()
            return json.dumps(temp)
        else:
            return json.dumps({
                "code":1,
                "desc":"not exit"
            })


# class AA(Resource):
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#
#
# if __name__ == '__main__':
#     a = AA("1","2")
#     print(a.__dict__)
#     print(json.dumps(a.__dict__))
#     # print(json.dumps(a))