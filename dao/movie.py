from dao.model.movie import Movie
from sqlalchemy import desc


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, limit: int = None, offset: int = None, status: bool = False):
        movies = self.session.query(Movie)
        if status:
            movies = movies.order_by(desc(Movie.year))
        if limit:
            movies = movies.limit(limit).offset(offset)
        
        return movies.all()

    def get_by_filter(self, filters, limit: int = None, offset: int = None, status: bool = False):
        movies = self.session.query(Movie)
        for attr, value in filters.items():
            movies = movies.filter(getattr(Movie, attr).like("%%%s%%" % value))
        if status:
            movies = movies.order_by(desc(Movie.year))
        if limit:
            movies = movies.limit(limit).offset(offset)
        
        return movies.all()

    def get_one(self, mid: int):
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def create(self, data):
        movies = Movie(**data)

        self.session.add(movies)
        self.session.commit()

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def update_partial(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):

        self.session.delete(movie)
        self.session.commit()
