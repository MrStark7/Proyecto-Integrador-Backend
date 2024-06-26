import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'tu_clave_secreta_para_jwt'
    
    # Configuración de Flask-Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.example.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'tu_email@example.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'tu_contraseña'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://tu_usuario:tu_contraseña@localhost/nombre_de_tu_bd'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://tu_usuario:tu_contraseña@localhost/nombre_de_tu_bd'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
