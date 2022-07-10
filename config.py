
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3}
    # SECRET_HERE = '249y823r9v8238r9u'
