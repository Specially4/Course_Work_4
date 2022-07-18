from dao.movie import MovieDAO
from utils import make_dict, get_length_page


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, attributes: dict = None):
        movies = self.dao.get_all()
        if attributes:
            status_dict, filter_dict = make_dict(attributes)
            
            match status_dict:
                case {"page": int(page), "status": "new"} if filter_dict:
                    movies = self.dao.get_by_filter(
                            filters=filter_dict,
                            limit=get_length_page(page)['limit'],
                            offset=get_length_page(page)['offset'],
                            status=status_dict['status']
                    )
                case {"page": int(page)} if filter_dict:
                    movies = self.dao.get_by_filter(
                            filters=filter_dict,
                            limit=get_length_page(page)['limit'],
                            offset=get_length_page(page)['offset']
                    )
                case {"page": int(page)} if not filter_dict:
                    movies = self.dao.get_all(
                        limit=get_length_page(page)['limit'], 
                        offset=get_length_page(page)['offset']
                    )
                case {"page": int(page), "status": "new"} if  not filter_dict:
                    movies = self.dao.get_all(
                        limit=get_length_page(page)['limit'],
                        offset=get_length_page(page)['offset'],
                        status=status_dict['status']
                    )
                case {"status": "new"} if filter_dict:
                    movies = self.dao.get_by_filter(
                            filters=filter_dict,
                            status=status_dict['status']
                    )
                case {"status": "new"} if not filter_dict:
                    movies = self.dao.get_all(status=status_dict['status'])
                case _ if filter_dict:
                    movies = self.dao.get_by_filter(filters=filter_dict)
                case _ if not filter_dict:
                    movies = self.dao.get_all()

        return movies

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.update(movie)

        return movie

    def update_partial(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

        return movie

    def delete(self, mid: int):
        movie = self.get_one(mid)

        self.dao.delete(movie)
