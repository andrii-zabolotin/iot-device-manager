from aiohttp import web
from peewee import DoesNotExist

from src.database import db
from src.services.device import DeviceService


async def create_device(request):
    data = await request.json()
    device = DeviceService().create(data=data, db=db)
    return web.json_response({'id': device.id})


async def list_device(request):
    return web.json_response(DeviceService().list(db=db))


async def get_device(request):
    id = int(request.match_info['id'])
    try:
        device = DeviceService().get(id=id, db=db)
    except DoesNotExist:
        return web.json_response({'error': 'Device with the specified id was not found'}, status=404)

    return web.json_response(device.__data__)


async def update_device(request):
    id = int(request.match_info['id'])
    data = await request.json()
    try:
        updated_device = DeviceService().update(data=data, db=db, id=id)
        return web.json_response(updated_device.__data__)
    except DoesNotExist:
        return web.json_response({'error': 'Device with the specified id was not found'}, status=404)


async def delete_device(request):
    id = int(request.match_info['id'])
    try:
        DeviceService().delete(db=db, id=id)
        return web.json_response(status=200)
    except DoesNotExist:
        return web.json_response({'error': 'Device with the specified id was not found'}, status=404)

