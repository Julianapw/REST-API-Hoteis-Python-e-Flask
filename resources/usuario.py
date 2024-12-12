from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_acess_token
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, get_raw_jwt
from blacklist import BLACKLIST


class User(Resource):
    
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()   
        return {"message":"User not found."}, 404
    
    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {"message":"An error ocurred trying to delete user."}, 500
            return {"message":"User deleted."}
        return {"message": "User not found."}, 404
    
class UserRegistros(Resource):
    #cadastro
    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
        atributos.add_argument('senha', type=str, required=True, help="The field 'login' cannot be left blank")
        dados = atributos.parse_args()
            
        if User.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists.".format(dados['login'])}
            
        user = UserModel(**dados)
        user.save_user()
        return{"message": "User created successfully!"},201

class UserLogin(Resource):
    
    @classmethod
    def post(cls):
        atributos = reqparse.RequestParser()
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados["login"])
        
        if user and safe_str_cmp(user.senha, dados["senha"]):
            token_de_acesso = create_acess_token(identity=user.user_id)
            return{"acess_token": token_de_acesso}, 200
        return {"message": "The username or password is incorrect"}, 401 #Unauthorized

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return{"message":"Looged out successfully!"}, 200