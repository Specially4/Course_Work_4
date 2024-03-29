from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did: int):
        return self.dao.get_one(did)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get('id')
        director = self.get_one(did)

        director.name = data.get('name')

        self.dao.update(director)

    def update_partial(self, data):
        did = data.get('id')

        director = self.get_one(did)

        if 'name' in data:
            director.name = data.get('name')

        self.dao.update(director)

    def delete(self, did: int):
        director = self.get_one(did)

        self.dao.delete(director)
