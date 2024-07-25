from abc import ABC, abstractmethod
from typing import Type

from peewee import Database, DoesNotExist

from src.models import BaseModel


class IRepository(ABC):
    @abstractmethod
    def __init__(self, model: Type[BaseModel], db: Database):
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, data: dict):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError


class PeeweeRepository(IRepository):
    def __init__(self, model: Type[BaseModel], db: Database):
        self._model = model
        self._db = db

    def get(self, id: int):
        with self._db:
            return self._model.get_or_none(self._model.id == id)

    def list(self):
        with self._db:
            return self._model.list()

    def create(self, data: dict):
        with self._db:
            return self._model.create(**data)

    def update(self, id: int, data: dict):
        with self._db:
            query = self._model.update(**data).where(self._model.id == id)
            query.execute()
            return self._model.get_by_id(id)

    def delete(self, id: int) -> None:
        with self._db:
            object = self._model.get_or_none(self._model.id == id)
            if not object:
                raise DoesNotExist

            query = self._model.delete().where(self._model.id == id)
            query.execute()
