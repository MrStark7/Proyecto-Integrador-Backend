from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Appointment
from .app import db

# VISTA DE CITAS
bp = Blueprint('appointment', __name__, url_prefix='/appointment')
api = Api(bp)

class AppointmentList(Resource):
    def get(self):
        appointments = Appointment.query.all()
        return [
            {
                'id': appointment.id,
                'date': appointment.date,
                'user_id': appointment.user_id,
                'service_id': appointment.service_id
            }
            for appointment in appointments
        ]

    def post(self):
        data = request.get_json()
        new_appointment = Appointment(
            date=data.get('date'),
            user_id=data.get('user_id'),
            service_id=data.get('service_id')
        )
        db.session.add(new_appointment)
        db.session.commit()
        return {
            'id': new_appointment.id,
            'date': new_appointment.date,
            'user_id': new_appointment.user_id,
            'service_id': new_appointment.service_id
        }, 201

class AppointmentResource(Resource):
    def get(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        return {
            'id': appointment.id,
            'date': appointment.date,
            'user_id': appointment.user_id,
            'service_id': appointment.service_id
        }

    def put(self, appointment_id):
        data = request.get_json()
        appointment = Appointment.query.get_or_404(appointment_id)
        appointment.date = data.get('date')
        appointment.user_id = data.get('user_id')
        appointment.service_id = data.get('service_id')
        db.session.commit()
        return {
            'id': appointment.id,
            'date': appointment.date,
            'user_id': appointment.user_id,
            'service_id': appointment.service_id
        }

    def delete(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return '', 204

api.add_resource(AppointmentList, '/')
api.add_resource(AppointmentResource, '/<int:appointment_id>')
