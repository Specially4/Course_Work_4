from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from setup_db import db

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

