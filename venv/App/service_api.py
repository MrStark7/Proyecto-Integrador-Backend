# service_api.py

from flask import request, jsonify
from flask_restful import Api, Resource, abort
from .models import Service, db
from .app import app

api = Api(app)

class ServiceList(Resource):
    def get(self):
        services = Service.query.all()
        return [{'id': service.id, 'name': service.name, 'description': service.description, 'category': service.category} for service in services], 200

    def post(self):
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        if not all(k in data for k in ('name', 'description', 'category', 'provider_id', 'available_slots')):
            return {'message': 'Missing fields in request'}, 400

        new_service = Service(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            provider_id=data['provider_id'],
            available_slots=data['available_slots']
        )
        db.session.add(new_service)
        db.session.commit()
        return {'message': 'Service created successfully'}, 201

api.add_resource(ServiceList, '/service')

class ServiceDetail(Resource):
    def get(self, service_id):
        service = Service.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        return {
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'category': service.category,
            'available_slots': service.available_slots,
            'provider_id': service.provider_id
        }, 200

    def put(self, service_id):
        service = Service.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        if not all(k in data for k in ('name', 'description', 'category', 'available_slots')):
            return {'message': 'Missing fields in request'}, 400

        service.name = data['name']
        service.description = data['description']
        service.category = data['category']
        service.available_slots = data['available_slots']
        db.session.commit()
        return {'message': 'Service updated successfully'}, 200

    def delete(self, service_id):
        service = Service.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        
        db.session.delete(service)
        db.session.commit()
        return {'message': 'Service deleted successfully'}, 200

api.add_resource(ServiceDetail, '/service/<int:service_id>')
