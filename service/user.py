import base64
import hashlib
import hmac
import calendar
import datetime

import jwt
from constants import PWD_HASH_ALGO, PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGO
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all_users(self):
        return self.dao.get_all_users()

    def get_one_user(self, uid: int):
        return self.dao.get_one_user(uid)

    def get_filter_by_name(self, username):
        return self.dao.get_filter_by_name(username)

    def add_users(self, data):
        data["password"] = self.get_hash(data.get('password'))
        return self.dao.add_users(data)

    def update_user(self, data):
        uid = data.get('id')
        user = self.get_one_user(uid)

        user.username = data.get('username')
        user.password = self.get_hash(data.get('password'))
        user.role = data.get('role')

        self.dao.update_user(user)

    def update_partial(self, data):
        uid = data.get('id')

        user = self.get_one_user(uid)

        if 'username' in data:
            user.username = data.get('username')
        if 'password' in data:
            user.password = self.get_hash(data.get('password'))
        if 'role' in data:
            user.role = data.get('role')

        self.dao.update_user(user)

    def delete(self, uid: int):
        user = self.get_one_user(uid)

        self.dao.delete(user)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            PWD_HASH_ALGO,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(PWD_HASH_ALGO, other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )

    def get_jwt(self, data):
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)
        tokens = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return tokens

    def check_token(self, token):
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
