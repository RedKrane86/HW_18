from flask import request
from flask_restx import Resource, Namespace

from app.container import movies_services
from app.dao.models.movies import MovieSchema

movies_ns = Namespace('movies')


@movies_ns.route('')
class MoviesView(Resource):
    def get(self):
        movies = movies_services.get_all()
        result = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        req_json = request.json
        movies_services.create(req_json)
        return '', 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get_one(self, mid):
        movie = movies_services.get_one(mid)
        result = MovieSchema().dump(movie)
        if not movie:
            return '', 404
        return result, 200

    def put(self, mid):
        req_json = request.json
        movie = movies_services.update(req_json)
        if not movie:
            return '', 404
        return '', 204

    def delete(self, mid):
        movie = movies_services.delete(mid)
        if not movie:
            return '', 404
        return '', 204
