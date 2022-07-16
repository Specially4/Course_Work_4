from flask import request, abort
from flask_restx import Namespace, Resource

from decorator import auth_required
from container import user_service
from dao.model.user import users_schema, user_schema

users_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        data = request.json
        user_service.create(data)
        return {'message': 'Object appended'}, 201

    def delete(self):
        pass


@users_ns.route('/<int:did>')
class UserView(Resource):
    @auth_required
    def get(self, did: int):
        user = user_service.get_one(did)
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
        user = user_service.update(req_json)
        if user:
            return {'message': 'Object updated'}, 204
        return {'message': 'Object not found'}, 400

    @auth_required
    def delete(self, did: int):
        user = user_service.delete(did)
        if user:
            return {'message': 'Object deleted'}, 204
        return {'message': 'Object not found'}, 400


@users_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self):
        req_json = request.json
        old_password = req_json['password_1']
        new_password = req_json['password_2']
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        email = user_service.check_token(token)['email']
        user = user_service.get_filter_by_name(email)
        uid = user.id

        data = {'id': uid, 'password': new_password}

        try:
            user_service.compare_passwords(user.password, old_password)
        except Exception as e:
            abort(401, message=str(e))

        user_service.update_partial(data)

        return {'message': 'Password changed'}, 200
