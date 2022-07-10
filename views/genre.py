from flask import request
from flask_restx import Namespace, Resource

from decorator import auth_required, admin_required
from container import genre_service
from dao.model.genre import genres_schema, genre_schema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all_genres()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        genre_service.add_genres(req_json)

        return 'Object appended', 201

    def delete(self):
        pass


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid: int):
        genre = genre_service.get_one_genre(gid)
        if genre:
            return genre_schema.dump(genre), 200
        return 'Object not found', 404

    @admin_required
    def path(self, gid: int):
        req_json = request.json
        req_json['id'] = gid
        genre = genre_service.update_partial(req_json)
        if genre:
            return 'Object updated', 204
        return 'Object not found', 404

    @admin_required
    def put(self, gid: int):
        req_json = request.json
        req_json['id'] = gid
        genre = genre_service.update_genre(req_json)
        if genre:
            return 'Object updated', 204
        return 'Object not found', 404

    @admin_required
    def delete(self, gid: int):
        genre_service.delete(gid)
        return 'Object deleted', 204
