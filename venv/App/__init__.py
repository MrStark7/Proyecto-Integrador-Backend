from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt = JWTManager(app)

    with app.app_context():
        # Importa y registra los Blueprints
        from .user_views import bp as user_bp
        from .service_views import bp as service_bp
        from .review_views import bp as review_bp
        from .appointment_views import bp as appointment_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(service_bp)
        app.register_blueprint(review_bp)
        app.register_blueprint(appointment_bp)

        return app
