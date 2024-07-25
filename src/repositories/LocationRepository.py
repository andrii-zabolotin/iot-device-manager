from peewee import Database

from src.models import Location
from src.repositories.IRepository import PeeweeRepository


class LocationRepository(PeeweeRepository):
    def __init__(self, db: Database):
        super().__init__(model=Location, db=db)
