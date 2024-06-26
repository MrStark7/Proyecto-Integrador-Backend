from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=True)
    apellido = db.Column(db.String(255), nullable=True)
    direccion = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True, unique=True)
    telefono = db.Column(db.String(255), nullable=True)
    contraseña = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)

class Servicio(db.Model):
    __tablename__ = 'servicios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=True)
    direccion = db.Column(db.String(255), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    horario = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.Date, nullable=True)
    numerocontacto = db.Column(db.String(255), nullable=True)
    ventastotales = db.Column(db.Integer, nullable=True)
    contador = db.Column(db.Integer, nullable=True)
    categoria = db.Column(db.String(255), nullable=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    service_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Appointment(db.Model):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    appointment_time = db.Column(db.DateTime, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('servicios.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
