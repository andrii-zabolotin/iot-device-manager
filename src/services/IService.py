from abc import ABC, abstractmethod

from peewee import Database


class IService(ABC):

    @abstractmethod
    def create(self, device_data: dict, db: Database):
        pass

    @abstractmethod
    def get(self, device_id: int, db: Database):
        pass

    @abstractmethod
    def list(self, db: Database):
        pass

    @abstractmethod
    def update(self, device_id: int, device_data: dict, db: Database):
        pass

    @abstractmethod
    def delete(self, device_id: int, db: Database) -> None:
        pass
    