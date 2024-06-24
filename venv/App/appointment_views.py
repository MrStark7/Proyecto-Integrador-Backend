from flask import Blueprint, request
from flask_restful import Api, Resource
from app.models import Appointment
from app import db
#VISTA DE CITAS

bp = Blueprint('appointment', __name__, url_prefix='/appointment') 
api = Api(bp)

class AppointmentList(Resource):
    def get(self):
        appointments = Appointment.query.all()
        return [{'id': appointment.id
