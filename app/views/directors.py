from flask_restx import Resource, Namespace

from app.container import director_services
from app.dao.models.directors import DirectorSchema

director_ns = Namespace('directors')

@director_ns.route('')
class DirectorsView(Resource):
    def get(self):
        directors = director_services.get_all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get_one(self, did):
        director = director_services.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200
