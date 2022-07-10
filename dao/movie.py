from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, limit=1, offset=0):
        movies = self.session.query(Movie).limit(limit).offset(offset)
        return movies

    def get_by_filter(self, filters):
        movies = self.session.query(Movie)
        for attr, value in filters.items():
            movies = movies.filter(getattr(Movie, attr).like("%%%s%%" % value))
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
