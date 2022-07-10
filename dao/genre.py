from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid: int):
        return self.session.query(Genre).get(gid)

    def create(self, data):
        genres = Genre(**data)

        self.session.add(genres)
        self.session.commit()

    def update(self, genre):

        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, genre):

        self.session.delete(genre)
        self.session.commit()
