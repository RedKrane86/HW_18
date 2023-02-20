from app.dao.models.directors import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors_all = Director.query.all()
        return directors_all

    def get_one(self, did):
        directors_one = Director.query.get(did)
        return directors_one

