from peewee import Database

from src.models import Device
from src.repositories.IRepository import PeeweeRepository


class DeviceRepository(PeeweeRepository):
    def __init__(self, db: Database):
        super().__init__(model=Device, db=db)
