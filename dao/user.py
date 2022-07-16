from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, uid: int):
        return self.session.query(User).filter(User.id == uid).first()

    def get_filter_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

    def update(self, user):

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user):

        self.session.delete(user)
        self.session.commit()
