from flask import Blueprint, request
from flask_restful import Api, Resource
from .app import Servicio
from sqlalchemy.sql import func
from .app import db

bp = Blueprint('reports', __name__, url_prefix='/reports')
api = Api(bp)

class ServiceReport(Resource):
    def get(self, provider_id):
        total_sales = db.session.query(func.sum(Servicio.ventastotales)).filter_by(proveedor_id=provider_id).scalar()
        sales_by_month = db.session.query(func.date_trunc('month', Servicio.fecha), func.sum(Servicio.ventastotales)).filter_by(proveedor_id=provider_id).group_by(func.date_trunc('month', Servicio.fecha)).all()
        top_services = Servicio.query.filter_by(proveedor_id=provider_id).order_by(Servicio.ventastotales.desc()).limit(5).all()

        return {
            'total_sales': total_sales,
            'sales_by_month': [{'month': month, 'sales': sales} for month, sales in sales_by_month],
            'top_services': [{'id': service.id, 'nombre': service.nombre, 'ventas': service.ventastotales} for service in top_services]
        }, 200

api.add_resource(ServiceReport, '/service/<int:provider_id>')
