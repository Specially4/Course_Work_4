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

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid: int):
        return self.dao.get_one(uid)

    def get_filter_by_name(self, email):
        return self.dao.get_filter_by_email(email)

    def create(self, data):
        data["password"] = self.get_hash(data.get('password'))
        return self.dao.create(data)

    def update(self, data):
        uid = data.get('id')
        user = self.get_one(uid)

        user.email = data.get('email')
        user.password = self.get_hash(data.get('password'))
        user.role = data.get('role')

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get('id')

        user = self.get_one(uid)

        if 'email' in data:
            user.email = data.get('email')
        if 'name' in data:
            user.name = self.get_hash(data.get('name'))
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'password' in data:
            user.password = self.get_hash(data.get('password'))
        if 'favorite_genre' in data:
            user.favorite_genre = data.get('favorite_genre')

        self.dao.update(user)

    def delete(self, uid: int):
        user = self.get_one(uid)

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
