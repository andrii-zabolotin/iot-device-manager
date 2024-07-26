from peewee import Database

from src.repositories.user import UserRepository
from src.services.IService import IService


class UserService(IService):
    def __init__(self):
        self.account_repository = UserRepository

    def create(self, data: dict, db: Database):
        return self.account_repository(db=db).create(data=data)

    def get(self, id: int, db: Database):
        return self.account_repository(db=db).get(id=id)

    def list(self, db: Database):
        return self.account_repository(db=db).list()

    def update(self, id: int, data: dict, db: Database):
        return self.account_repository(db=db).update(id=id, data=data)

    def delete(self, id: int, db: Database) -> None:
        self.account_repository(db=db).delete(id=id)
