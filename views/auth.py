from flask import request, abort
from flask_restx import Namespace, Resource

from container import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            abort(400)

        user = user_service.get_filter_by_name(username)

        if user is None:
            abort(401)

        try:
            user_service.compare_passwords(user.password, password)
        except Exception as e:
            abort(401)

        data = {
            'username': user.username,
            'role': user.role
        }
        tokens = user_service.get_jwt(data)
        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)
        if refresh_token is None:
            abort(400)

        try:
            data = user_service.check_token(refresh_token)
        except Exception as e:
            abort(400)

        username = data.get('username')

        user = user_service.get_filter_by_name(username)

        data = {
            'username': user.username,
            'role': user.role
        }
        tokens = user_service.get_jwt(data)
        return tokens, 201
