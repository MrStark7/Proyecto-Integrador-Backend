from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Usuario, db
from werkzeug.security import generate_password_hash
from flask_mail import Message, Mail
from .app import app

mail = Mail(app)
bp = Blueprint('password_reset', __name__, url_prefix='/password_reset')
api = Api(bp)

class RequestPasswordReset(Resource):
    def post(self):
        data = request.get_json()
        user = Usuario.query.filter_by(email=data['email']).first()
        if not user:
            return {'message': 'User not found'}, 404
        
        token = create_reset_token(user)
        send_reset_email(user.email, token)
        return {'message': 'Password reset email sent'}, 200

def create_reset_token(user):
    pass

def send_reset_email(email, token):
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('password_reset.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

class PasswordReset(Resource):
    def post(self, token):
        user = verify_reset_token(token)
        if not user:
            return {'message': 'Invalid or expired token'}, 400
        
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'], method='sha256')
        user.contraseña = hashed_password
        db.session.commit()
        return {'message': 'Password has been reset'}, 200

def verify_reset_token(token):
    # Implement token verification logic here
    pass

api.add_resource(RequestPasswordReset, '/request')
api.add_resource(PasswordReset, '/reset/<token>')
