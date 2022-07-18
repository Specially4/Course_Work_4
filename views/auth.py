from flask import request, abort
from flask_restx import Namespace, Resource

from container import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)
        if None in [email, password]:
            abort(400)

        data = {
            'email': email,
            'password': password
        }

        try:
            user = user_service.create(data)
        except Exception as e:
            abort(400, message=str(e))

        return 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)
        if None in [email, password]:
            abort(400)

        user = user_service.get_filter_by_email(email)

        if user is None:
            abort(401)

        try:
            status = user_service.compare_passwords(user.password, password)
        except Exception as e:
            abort(401, message=str(e))
        
        if status:
            data = {
                'email': user.email
            }
            tokens = user_service.get_jwt(data)
            return tokens, 201
        else:
            abort(401)

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)
        if refresh_token is None:
            abort(400)

        try:
            data = user_service.check_token(refresh_token)
        except Exception as e:
            abort(400)

        email = data.get('email')

        user = user_service.get_filter_by_email(email)

        data = {
            'email': user.email
        }
        tokens = user_service.get_jwt(data)
        return tokens, 201
