from flask import request
from flask_restx import Namespace, Resource

from decorator import auth_required
from container import movie_service
from dao.model.movie import movies_schema, movie_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        req_args = dict(request.args)
        movies = movie_service.get_all(attributes=req_args)
        if len(movies_schema.dump(movies)) == 0:
            return 'Invalid variables specified', 404

        return movies_schema.dump(movies), 200

    @auth_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return 'Movie appended', 201

    def delete(self):
        pass


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        return 'Movie not found', 404

    @auth_required
    def path(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update_partial(req_json)
        if movie:
            return 'Movie updated', 204
        return 'Movie not found', 404

    @auth_required
    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie = movie_service.update(req_json)
        if movie:
            return 'Movie updated', 204
        return 'Movie not found', 404

    @auth_required
    def delete(self, mid: int):
        movie = movie_service.delete(mid)
        if movie:
            return 'Movie not found', 404
        return 'Movie deleted', 204
