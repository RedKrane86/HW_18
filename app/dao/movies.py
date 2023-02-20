from flask import request

from app.dao.models.movies import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        stmt = Movie.query
        if director_id:
            stmt = stmt.filter(Movie.director_id == director_id)
        if genre_id:
            stmt = stmt.filter(Movie.genre_id == genre_id)
        if year:
            stmt = stmt.filter(Movie.year == year)
        movies = stmt.all()
        return movies

    def get_one(self, mid):
        movie_single = self.session.query(Movie).get(mid)
        return movie_single

    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()