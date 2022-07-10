from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did: int):
        return self.session.query(Director).get(did)

    def create(self, data):
        directors = Director(**data)

        self.session.add(directors)
        self.session.commit()

    def update(self, director):

        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, director):

        self.session.delete(director)
        self.session.commit()
