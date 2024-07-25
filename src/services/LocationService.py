from peewee import Database

from src.repositories.LocationRepository import LocationRepository
from src.services.IService import IService


class LocationService(IService):
    def __init__(self):
        self.location_repository = LocationRepository

    def create(self, data: dict, db: Database):
        return self.location_repository(db=db).create(data=data)

    def get(self, id: int, db: Database):
        return self.location_repository(db=db).get(id=id)

    def list(self, db: Database):
        return self.location_repository(db=db).list()

    def update(self, id: int, data: dict, db: Database):
        return self.location_repository(db=db).update(id=id, data=data)

    def delete(self, id: int, db: Database) -> None:
        self.location_repository(db=db).delete(id=id)