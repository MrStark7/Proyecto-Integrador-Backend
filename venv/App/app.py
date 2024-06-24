# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Importa el módulo que contiene las rutas de la API
from .app import user_views
from .app import service_views
from .app import review_views
from .app import appointment_views

if __name__ == '__main__':
    app.run(debug=True)
