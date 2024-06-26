from flask import request, jsonify
from flask_restful import Api, Resource, abort
from .app import Servicio, db
from .app import app

api = Api(app)

class ServiceList(Resource):
    def get(self):
        services = Servicio.query.all()
        return [
            {
                'id': service.id,
                'nombre': service.nombre,
                'direccion': service.direccion,
                'descripcion': service.descripcion,
                'horario': service.horario,
                'fecha': service.fecha,
                'numerocontacto': service.numerocontacto,
                'ventastotales': service.ventastotales,
                'contador': service.contador,
                'categoria': service.categoria,
                'proveedor_id': service.proveedor_id
            }
            for service in services
        ], 200

    def post(self):
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        required_fields = ['nombre', 'direccion', 'descripcion', 'horario', 'fecha', 'numerocontacto', 'ventastotales', 'contador', 'categoria', 'proveedor_id']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing fields in request'}, 400

        new_service = Servicio(
            nombre=data['nombre'],
            direccion=data['direccion'],
            descripcion=data['descripcion'],
            horario=data['horario'],
            fecha=data['fecha'],
            numerocontacto=data['numerocontacto'],
            ventastotales=data['ventastotales'],
            contador=data['contador'],
            categoria=data['categoria'],
            proveedor_id=data['proveedor_id']
        )
        db.session.add(new_service)
        db.session.commit()
        return {'message': 'Service created successfully'}, 201

api.add_resource(ServiceList, '/service')

class ServiceDetail(Resource):
    def get(self, service_id):
        service = Servicio.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        return {
            'id': service.id,
            'nombre': service.nombre,
            'direccion': service.direccion,
            'descripcion': service.descripcion,
            'horario': service.horario,
            'fecha': service.fecha,
            'numerocontacto': service.numerocontacto,
            'ventastotales': service.ventastotales,
            'contador': service.contador,
            'categoria': service.categoria,
            'proveedor_id': service.proveedor_id
        }, 200

    def put(self, service_id):
        service = Servicio.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        
        data = request.get_json()
        if not data:
            return {'message': 'No input data provided'}, 400

        required_fields = ['nombre', 'direccion', 'descripcion', 'horario', 'fecha', 'numerocontacto', 'ventastotales', 'contador', 'categoria']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing fields in request'}, 400

        service.nombre = data['nombre']
        service.direccion = data['direccion']
        service.descripcion = data['descripcion']
        service.horario = data['horario']
        service.fecha = data['fecha']
        service.numerocontacto = data['numerocontacto']
        service.ventastotales = data['ventastotales']
        service.contador = data['contador']
        service.categoria = data['categoria']
        service.proveedor_id = data.get('proveedor_id', service.proveedor_id)
        db.session.commit()
        return {'message': 'Service updated successfully'}, 200

    def delete(self, service_id):
        service = Servicio.query.get(service_id)
        if service is None:
            abort(404, message="Service {} doesn't exist".format(service_id))
        
        db.session.delete(service)
        db.session.commit()
        return {'message': 'Service deleted successfully'}, 200

api.add_resource(ServiceDetail, '/service/<int:service_id>')
