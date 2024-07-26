from peewee import Database

from src.repositories.device import DeviceRepository
from src.services.IService import IService


class DeviceService(IService):
    def __init__(self):
        self.device_repository = DeviceRepository

    def create(self, data: dict, db: Database):
        return self.device_repository(db=db).create(data=data)

    def get(self, id: int, db: Database):
        return self.device_repository(db=db).get(id=id)

    def list(self, db: Database):
        return self.device_repository(db=db).list()

    def update(self, id: int, data: dict, db: Database):
        return self.device_repository(db=db).update(id=id, data=data)

    def delete(self, id: int, db: Database) -> None:
        self.device_repository(db=db).delete(id=id)