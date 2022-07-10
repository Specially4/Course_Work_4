import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all(length_list=3)

        assert len(movie) > 0

    def test_create(self):
        movie_d = {
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2003,
            'rating': 0.5,
            'genre_id': 2,
            'director_id': 3
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            'id': 1,
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2003,
            'rating': 0.5,
            'genre_id': 2,
            'director_id': 3
        }
        self.movie_service.update(movie_d)