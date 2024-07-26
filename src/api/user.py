from aiohttp import web
from peewee import DoesNotExist

from src.database import db
from src.services.user import UserService


async def create_user(request):
    data = await request.json()
    user = UserService().create(data=data, db=db)
    return web.json_response({'id': user.id})


async def list_user(request):
    return web.json_response(UserService().list(db=db))


async def get_user(request):
    id = int(request.match_info['id'])
    try:
        user = UserService().get(id=id, db=db)
    except DoesNotExist:
        return web.json_response({'error': 'User with the specified id was not found'}, status=404)

    return web.json_response(user.__data__)


async def update_user(request):
    id = int(request.match_info['id'])
    data = await request.json()
    try:
        updated_user = UserService().update(data=data, db=db, id=id)
        return web.json_response(updated_user.__data__)
    except DoesNotExist:
        return web.json_response({'error': 'User with the specified id was not found'}, status=404)


async def delete_user(request):
    id = int(request.match_info['id'])
    try:
        UserService().delete(db=db, id=id)
        return web.json_response(status=200)
    except DoesNotExist:
        return web.json_response({'error': 'User with the specified id was not found'}, status=404)

