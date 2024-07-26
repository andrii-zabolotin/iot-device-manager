import pytest
from aiohttp import web

from src.api.location import *


@pytest.mark.asyncio
async def test_create_location(aiohttp_client, setup_database):
    data = {'name': 'Test Location'}

    app = web.Application()
    app.router.add_post('/location/create', create_location)
    client = await aiohttp_client(app)

    resp = await client.post('/location/create', json=data)
    assert resp.status == 200
    json_resp = await resp.json()
    assert 'id' in json_resp


@pytest.mark.asyncio
async def test_get_location(aiohttp_client, setup_database):
    data = {'name': 'Test Location'}

    app = web.Application()
    app.router.add_post('/location/create', create_location)
    app.router.add_get('/location/{id}', get_location)
    client = await aiohttp_client(app)

    create_resp = await client.post('/location/create', json=data)
    json_create_resp = await create_resp.json()
    location_id = json_create_resp['id']

    resp = await client.get(f'/location/{location_id}')
    assert resp.status == 200
    json_resp = await resp.json()
    assert json_resp['name'] == 'Test Location'


@pytest.mark.asyncio
async def test_update_location(aiohttp_client, setup_database):
    data = {'name': 'Test Location'}

    app = web.Application()
    app.router.add_post('/location/create', create_location)
    app.router.add_patch('/location/{id}', update_location)
    client = await aiohttp_client(app)

    create_resp = await client.post('/location/create', json=data)
    json_create_resp = await create_resp.json()
    location_id = json_create_resp['id']

    update_data = {'name': 'Updated Location'}
    resp = await client.patch(f'/location/{location_id}', json=update_data)
    assert resp.status == 200
    json_resp = await resp.json()
    assert json_resp['name'] == 'Updated Location'


@pytest.mark.asyncio
async def test_delete_location(aiohttp_client, setup_database):
    data = {'name': 'Test Location'}

    app = web.Application()
    app.router.add_post('/location/create', create_location)
    app.router.add_get('/location/{id}', get_location)
    app.router.add_delete('/location/{id}', delete_location)
    client = await aiohttp_client(app)

    create_resp = await client.post('/location/create', json=data)
    json_create_resp = await create_resp.json()
    location_id = json_create_resp['id']

    delete_resp = await client.delete(f'/location/{location_id}')
    assert delete_resp.status == 200

    get_resp = await client.get(f'/location/{location_id}')
    assert get_resp.status == 404
    json_resp = await get_resp.json()
    assert json_resp['error'] == 'Location with the specified id was not found'


@pytest.mark.asyncio
async def test_list_locations(aiohttp_client, setup_database):
    data1 = {'name': 'Location 1'}
    data2 = {'name': 'Location 2'}

    app = web.Application()
    app.router.add_post('/location/create', create_location)
    app.router.add_get('/location/list', list_location)
    client = await aiohttp_client(app)

    await client.post('/location/create', json=data1)
    await client.post('/location/create', json=data2)

    resp = await client.get('/location/list')
    assert resp.status == 200
    json_resp = await resp.json()
    assert len(json_resp) == 2
    assert any(location['name'] == 'Location 1' for location in json_resp)
    assert any(location['name'] == 'Location 2' for location in json_resp)
