from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.model.user import User
from dao.movie import MovieDAO
from dao.user import UserDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    first_movie = Movie(
        id=1,
        title='First_movie',
        description='',
        trailer='None',
        year=2000,
        rating=0,
        genre_id=2,
        director_id=3
    )
    second_movie = Movie(
        id=2,
        title='Second_movie',
        description='',
        trailer='None',
        year=2002,
        rating=0,
        genre_id=3,
        director_id=4
    )
    third_movie = Movie(
        id=3,
        title='Third_movie',
        description='',
        trailer='None',
        year=2003,
        rating=0,
        genre_id=4,
        director_id=5
    )

    movie_dao.get_one = MagicMock(return_value=first_movie)
    movie_dao.get_all = MagicMock(return_value=[first_movie, second_movie, third_movie])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    first_genre = Genre(id=1, name='Fantasy')
    second_genre = Genre(id=2, name='Detective')
    third_genre = Genre(id=3, name='Fiction')

    genre_dao.get_one = MagicMock(return_value=first_genre)
    genre_dao.get_all = MagicMock(return_value=[first_genre, second_genre, third_genre])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    first_director = Director(id=1, name='Ричард Келли')
    second_director = Director(id=2, name='Пит Доктер')
    third_director = Director(id=3, name='Шон Маккормак')

    director_dao.get_one = MagicMock(return_value=first_director)
    director_dao.get_all = MagicMock(return_value=[first_director, second_director, third_director])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    first_user = User(id=1, username='Ivan', password='password', role='admin')
    second_user = User(id=2, username='John', password='password', role='user')
    third_user = User(id=3, username='Mike', password='password', role='user')

    user_dao.get_one = MagicMock(return_value=first_user)
    user_dao.get_all = MagicMock(return_value=[first_user, second_user, third_user])
    user_dao.create = MagicMock(return_value=User(id=4))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
