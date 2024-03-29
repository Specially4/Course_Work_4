from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid: int):
        return self.dao.get_one(gid)

    def create(self, data):
        return self.dao.create(data)  # Добавлено возвращение для работы тестов, при необходимости удалить.

    def update(self, data):
        gid = data.get('id')
        genre = self.get_one(gid)

        genre.name = data.get('name')

        self.dao.update(genre)

    def update_partial(self, data):
        gid = data.get('id')
        genre = self.get_one(gid)

        if 'name' in data:
            genre.name = data.get('name')

        self.dao.update(genre)

    def delete(self, gid: int):
        genre = self.get_one(gid)

        self.dao.delete(genre)
