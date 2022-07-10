from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_one_user(self, uid: int):
        return self.session.query(User).filter(User.id == uid).first()

    def get_filter_by_name(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def add_users(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

    def update_user(self, user):

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user):

        self.session.delete(user)
        self.session.commit()
