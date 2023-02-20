from app.dao.directors import DirectorsDAO
from app.dao.genres import GenresDAO
from app.dao.movies import MoviesDAO
from app.services.directors import DirectorService
from app.services.genres import GenresService
from app.services.movies import MovieService
from setup_db import db

movies_dao = MoviesDAO(db.session)
movies_services = MovieService(movies_dao)

director_dao = DirectorsDAO(db.session)
director_services = DirectorService(director_dao)

genre_dao = GenresDAO(db.session)
genre_services = GenresService(genre_dao)
