from peewee import *

from src.database import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'api_user'

    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    @staticmethod
    def list():
        query = User.select()
        user_list = [user.__data__ for user in query]
        return user_list


class Location(BaseModel):
    class Meta:
        db_table = 'location'

    name = CharField()

    @staticmethod
    def list():
        query = Location.select()
        location_list = [location.__data__ for location in query]
        return location_list


class Device(BaseModel):
    class Meta:
        db_table = 'device'

    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    user = ForeignKeyField(User, backref='devices')

    @staticmethod
    def list():
        query = Device.select()
        device_list = [device.__data__ for device in query]
        return device_list
