from flask import Blueprint, request
from flask_restful import Api, Resource
from .models import Review
from .app import db

bp = Blueprint('review', __name__, url_prefix='/review')
api = Api(bp)

class ReviewList(Resource):
    def get(self):
        reviews = Review.query.all()
        return [{'id': review.id, 'rating': review.rating, 'comment': review.comment, 'service_id': review.service_id, 'user_id': review.user_id} for review in reviews]

    def post(self):
        data = request.get_json()
        new_review = Review(rating=data['rating'], comment=data['comment'], service_id=data['service_id'], user_id=data['user_id'])
        db.session.add(new_review)
        db.session.commit()
        return {'message': 'Review created successfully'}, 201

api.add_resource(ReviewList, '/')

class ReviewDetail(Resource):
    def get(self, review_id):
        review = Review.query.get_or_404(review_id)
        return {'id': review.id, 'rating': review.rating, 'comment': review.comment, 'service_id': review.service_id, 'user_id': review.user_id}

    def put(self, review_id):
        data = request.get_json()
        review = Review.query.get_or_404(review_id)
        review.rating = data['rating']
        review.comment = data['comment']
        db.session.commit()
        return {'message': 'Review updated successfully'}, 200

    def delete(self, review_id):
        review = Review.query.get_or_404(review_id)
        db.session.delete(review)
        db.session.commit()
        return {'message': 'Review deleted successfully'}, 200

api.add_resource(ReviewDetail, '/<int:review_id>')
