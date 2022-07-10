from flask import request, abort

from container import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user_service.check_token(token)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(400)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = user_service.check_token(token)
            role = user['role']
            if role != 'admin':
                abort(401)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(400)
        return func(*args, **kwargs)

    return wrapper
