from aiohttp import web
from peewee import DoesNotExist

from src.database import db
from src.services.location import LocationService


async def create_location(request):
    data = await request.json()
    location = LocationService().create(data=data, db=db)
    return web.json_response({'id': location.id})


async def list_location(request):
    return web.json_response(LocationService().list(db=db))


async def get_location(request):
    id = int(request.match_info['id'])
    location = LocationService().get(id=id, db=db)
    if not location:
        return web.json_response({'error': 'Location with the specified id was not found'}, status=404)

    return web.json_response(location.__data__)


async def update_location(request):
    id = int(request.match_info['id'])
    data = await request.json()
    try:
        updated_location = LocationService().update(data=data, db=db, id=id)
        return web.json_response(updated_location.__data__)
    except DoesNotExist:
        return web.json_response({'error': 'Location with the specified id was not found'}, status=404)


async def delete_location(request):
    id = int(request.match_info['id'])
    try:
        LocationService().delete(db=db, id=id)
        return web.json_response(status=200)
    except DoesNotExist:
        return web.json_response({'error': 'Location with the specified id was not found'}, status=404)

