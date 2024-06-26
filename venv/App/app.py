from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tu_usuario:tu_contraseña@localhost/nombre_de_tu_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importa los módulos que contienen las rutas de la API
from .app import user_views
from .app import service_views
from .app import review_views
from .app import appointment_views

# Registrar los Blueprints - es del Flask
app.register_blueprint(user_views.bp)
app.register_blueprint(service_views.bp)
app.register_blueprint(review_views.bp)
app.register_blueprint(appointment_views.bp)

if __name__ == '__main__':
    app.run(debug=True)
