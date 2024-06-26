from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_socketio import SocketIO

db = SQLAlchemy()
mail = Mail()
socketio = SocketIO()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    jwt = JWTManager(app)
    mail.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        # Importa y registra los Blueprints
        from .user_views import bp as user_bp
        from .services_views import bp as service_bp
        from .review_views import bp as review_bp
        from .appointment_views import bp as appointment_bp
        from .password_reset_views import bp as password_reset_bp
        from .report_views import bp as report_bp
        from .availability_views import bp as availability_bp
        from .tracking_views import bp as tracking_bp
        from .chat_views import bp as chat_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(service_bp)
        app.register_blueprint(review_bp)
        app.register_blueprint(appointment_bp)
        app.register_blueprint(password_reset_bp)
        app.register_blueprint(report_bp)
        app.register_blueprint(availability_bp)
        app.register_blueprint(tracking_bp)
        app.register_blueprint(chat_bp)

    return app
