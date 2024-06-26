from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Servicio
from .app import db

bp = Blueprint('service', __name__, url_prefix='/service')
api = Api(bp)

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
        ]

    def post(self):
        data = request.get_json()
        new_service = Servicio(
            nombre=data.get('nombre'),
            direccion=data.get('direccion'),
            descripcion=data.get('descripcion'),
            horario=data.get('horario'),
            fecha=data.get('fecha'),
            numerocontacto=data.get('numerocontacto'),
            ventastotales=data.get('ventastotales'),
            contador=data.get('contador'),
            categoria=data.get('categoria'),
            proveedor_id=data.get('proveedor_id')
        )
        db.session.add(new_service)
        db.session.commit()
        return {
            'id': new_service.id,
            'nombre': new_service.nombre,
            'direccion': new_service.direccion,
            'descripcion': new_service.descripcion,
            'horario': new_service.horario,
            'fecha': new_service.fecha,
            'numerocontacto': new_service.numerocontacto,
            'ventastotales': new_service.ventastotales,
            'contador': new_service.contador,
            'categoria': new_service.categoria,
            'proveedor_id': new_service.proveedor_id
        }, 201

api.add_resource(ServiceList, '/')

class ServiceDetail(Resource):
    def get(self, service_id):
        service = Servicio.query.get_or_404(service_id)
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
        }

    def put(self, service_id):
        data = request.get_json()
        service = Servicio.query.get_or_404(service_id)
        service.nombre = data.get('nombre')
        service.direccion = data.get('direccion')
        service.descripcion = data.get('descripcion')
        service.horario = data.get('horario')
        service.fecha = data.get('fecha')
        service.numerocontacto = data.get('numerocontacto')
        service.ventastotales = data.get('ventastotales')
        service.contador = data.get('contador')
        service.categoria = data.get('categoria')
        service.proveedor_id = data.get('proveedor_id')
        db.session.commit()
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
        }

    def delete(self, service_id):
        service = Servicio.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return {'message': 'Service deleted successfully'}, 200

api.add_resource(ServiceDetail, '/<int:service_id>')
