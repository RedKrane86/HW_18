from flask_restx import Resource, Namespace

from app.container import genre_services
from app.dao.models.genres import GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('')
class GenresView(Resource):
    def get(self):
        genres = genre_services.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_services.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200
