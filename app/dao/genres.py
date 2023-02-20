from app.dao.models.genres import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres_all = Genre.query.all()
        return genres_all

    def get_one(self, gid):
        genres_one = Genre.query.get(gid)
        return genres_one
