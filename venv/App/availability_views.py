from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Servicio, Appointment
from datetime import datetime
from .app import db

bp = Blueprint('availability', __name__, url_prefix='/availability')
api = Api(bp)

class CheckAvailability(Resource):
    def get(self, service_id, date):
        service = Servicio.query.get(service_id)
        if not service:
            return {'message': 'Service not found'}, 404

        appointments = Appointment.query.filter_by(service_id=service_id, appointment_time=date).all()
        if not appointments:
            return {'available_slots': service.available_slots}, 200

        booked_slots = [appt.appointment_time for appt in appointments]
        available_slots = [slot for slot in service.available_slots if slot not in booked_slots]
        return {'available_slots': available_slots}, 200

api.add_resource(CheckAvailability, '/check/<int:service_id>/<string:date>')
