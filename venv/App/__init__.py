from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app)

    from .views import user_views, service_views, review_views, appointment_views
    app.register_blueprint(user_views.bp)
    app.register_blueprint(service_views.bp)
    app.register_blueprint(review_views.bp)
    app.register_blueprint(appointment_views.bp)

    return app
