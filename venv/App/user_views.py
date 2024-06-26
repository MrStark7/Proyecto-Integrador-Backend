from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Usuario, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .app import app

bp = Blueprint('user', __name__, url_prefix='/user')
api = Api(bp)

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = Usuario(
            nombre=data['first_name'],
            apellido=data['last_name'],
            direccion=data.get('address', ''),
            email=data['email'],
            telefono=data['phone'],
            contraseña=hashed_password,
            tipo_usuario=data.get('tipo_usuario', 'Normal')
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = Usuario.query.filter_by(email=data['email']).first()
        if not user or not check_password_hash(user.contraseña, data['password']):
            return {'message': 'Invalid credentials'}, 401
        access_token = create_access_token(identity={'nombre': user.nombre, 'email': user.email})
        return {'access_token': access_token}, 200

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
