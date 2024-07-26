import pytest
from aiohttp import web

from src.api.device import *


@pytest.mark.asyncio
async def test_create_device(aiohttp_client, setup_database, get_location, get_user):
    data = {
        'name': 'Test Device',
        'type': 'Test Type',
        'login': 'testlogin',
        'password': 'testpassword',
        'location': get_location.id,
        'user': get_user.id
    }

    app = web.Application()
    app.router.add_post('/device/create', create_device)
    client = await aiohttp_client(app)

    resp = await client.post('/device/create', json=data)
    assert resp.status == 200
    json_resp = await resp.json()
    assert 'id' in json_resp


@pytest.mark.asyncio
async def test_list_devices(aiohttp_client, setup_database, get_location, get_user):
    data1 = {
        'name': 'Device 1',
        'type': 'Type 1',
        'login': 'login1',
        'password': 'password1',
        'location': get_location.id,
        'user': get_user.id
    }
    data2 = {
        'name': 'Device 2',
        'type': 'Type 2',
        'login': 'login2',
        'password': 'password2',
        'location': get_location.id,
        'user': get_user.id
    }

    app = web.Application()
    app.router.add_post('/device/create', create_device)
    app.router.add_get('/device/list', list_device)
    client = await aiohttp_client(app)

    await client.post('/device/create', json=data1)
    await client.post('/device/create', json=data2)

    resp = await client.get('/device/list')
    assert resp.status == 200
    json_resp = await resp.json()
    assert len(json_resp) == 2


@pytest.mark.asyncio
async def test_get_device(aiohttp_client, setup_database, get_location, get_user):
    data = {
        'name': 'Test Device',
        'type': 'Test Type',
        'login': 'testlogin',
        'password': 'testpassword',
        'location': get_location.id,
        'user': get_user.id
    }

    app = web.Application()
    app.router.add_post('/device/create', create_device)
    app.router.add_get('/device/{id}', get_device)
    client = await aiohttp_client(app)

    create_resp = await client.post('/device/create', json=data)
    assert create_resp.status == 200
    json_create_resp = await create_resp.json()
    device_id = json_create_resp['id']

    get_resp = await client.get(f'/device/{device_id}')
    assert get_resp.status == 200
    json_get_resp = await get_resp.json()
    assert json_get_resp['id'] == device_id
    assert json_get_resp['name'] == data['name']


@pytest.mark.asyncio
async def test_update_device(aiohttp_client, setup_database, get_location, get_user):
    create_data = {
        'name': 'Old Device',
        'type': 'Old Type',
        'login': 'oldlogin',
        'password': 'oldpassword',
        'location': get_location.id,
        'user': get_user.id
    }

    update_data = {
        'name': 'Updated Device',
        'type': 'Updated Type',
        'login': 'updatedlogin',
        'password': 'updatedpassword'
    }

    app = web.Application()
    app.router.add_post('/device/create', create_device)
    app.router.add_patch('/device/{id}', update_device)
    app.router.add_get('/device/{id}', get_device)
    client = await aiohttp_client(app)

    create_resp = await client.post('/device/create', json=create_data)
    assert create_resp.status == 200
    json_create_resp = await create_resp.json()
    device_id = json_create_resp['id']

    update_resp = await client.patch(f'/device/{device_id}', json=update_data)
    assert update_resp.status == 200

    get_resp = await client.get(f'/device/{device_id}')
    assert get_resp.status == 200
    json_get_resp = await get_resp.json()
    assert json_get_resp['name'] == update_data['name']
    assert json_get_resp['type'] == update_data['type']


@pytest.mark.asyncio
async def test_delete_device(aiohttp_client, setup_database, get_location, get_user):
    data = {
        'name': 'Device to Delete',
        'type': 'Type to Delete',
        'login': 'logintodelete',
        'password': 'passwordtodelete',
        'location': get_location.id,
        'user': get_user.id
    }

    app = web.Application()
    app.router.add_post('/device/create', create_device)
    app.router.add_delete('/device/{id}', delete_device)
    app.router.add_get('/device/list', list_device)
    app.router.add_get('/device/{id}', get_device)
    client = await aiohttp_client(app)

    create_resp = await client.post('/device/create', json=data)
    assert create_resp.status == 200
    json_create_resp = await create_resp.json()
    device_id = json_create_resp['id']

    delete_resp = await client.delete(f'/device/{device_id}')
    assert delete_resp.status == 200

    get_resp = await client.get(f'/device/{device_id}')
    assert get_resp.status == 404
    json_resp = await get_resp.json()
    assert json_resp['error'] == 'Device with the specified id was not found'
