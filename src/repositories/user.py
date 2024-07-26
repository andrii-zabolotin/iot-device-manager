from peewee import Database

from src.models import User
from src.repositories.IRepository import PeeweeRepository


class UserRepository(PeeweeRepository):
    def __init__(self, db: Database):
        super().__init__(model=User, db=db)
