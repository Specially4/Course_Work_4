from flask import request
from flask_restx import Namespace, Resource

from decorator import auth_required, admin_required
from container import user_service
from dao.model.user import users_schema, user_schema

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self):
        users = user_service.get_all_users()
        return users_schema.dump(users), 200

    def post(self):
        data = request.json
        users = user_service.add_users(data)
        return {'message': 'Object appended'}, 201

    def delete(self):
        pass


@users_ns.route('/<int:did>')
class UserView(Resource):
    @admin_required
    def get(self, did: int):
        user = user_service.get_one_user(did)
        if user:
            return user_schema.dump(user), 200
        return {'message': 'Object updated'}, 400

    @auth_required
    def path(self, did: int):
        req_json = request.json
        req_json['id'] = did
        user = user_service.update_partial(req_json)
        if user:
            return {'message': 'Object updated'}, 204
        return {'message': 'Object not found'}, 400

    @auth_required
    def put(self, did: int):
        req_json = request.json
        req_json['id'] = did
        user = user_service.update_user(req_json)
        if user:
            return {'message': 'Object updated'}, 204
        return {'message': 'Object not found'}, 400

    @admin_required
    def delete(self, did: int):
        user = user_service.delete(did)
        if user:
            return {'message': 'Object deleted'}, 204
        return {'message': 'Object not found'}, 400
