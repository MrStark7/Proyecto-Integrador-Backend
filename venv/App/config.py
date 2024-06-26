import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_secreta' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://tu_usuario:tu_contraseña@localhost/nombre_de_tu_bd'

class TestingConfig(Config):
    # Testeo
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
