import pytest

from src.api.user import *


@pytest.mark.asyncio
async def test_create_user(aiohttp_client, setup_database):
    data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

    app = web.Application()
    app.router.add_post('/user/create', create_user)
    client = await aiohttp_client(app)

    resp = await client.post('/user/create', json=data)
    assert resp.status == 200
    json_resp = await resp.json()
    assert 'id' in json_resp


@pytest.mark.asyncio
async def test_get_user(aiohttp_client, setup_database):
    data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

    app = web.Application()
    app.router.add_post('/user/create', create_user)
    app.router.add_get('/user/{id}', get_user)
    client = await aiohttp_client(app)

    create_resp = await client.post('/user/create', json=data)
    json_create_resp = await create_resp.json()
    user_id = json_create_resp['id']

    resp = await client.get(f'/user/{user_id}')
    assert resp.status == 200
    json_resp = await resp.json()
    assert json_resp['name'] == 'Test User'
    assert json_resp['email'] == 'test@example.com'


@pytest.mark.asyncio
async def test_update_user(aiohttp_client, setup_database):
    data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

    app = web.Application()
    app.router.add_post('/user/create', create_user)
    app.router.add_patch('/user/{id}', update_user)
    client = await aiohttp_client(app)

    create_resp = await client.post('/user/create', json=data)
    json_create_resp = await create_resp.json()
    user_id = json_create_resp['id']

    update_data = {'name': 'Updated User', 'email': 'updated@example.com'}
    resp = await client.patch(f'/user/{user_id}', json=update_data)
    assert resp.status == 200
    json_resp = await resp.json()
    assert json_resp['name'] == 'Updated User'
    assert json_resp['email'] == 'updated@example.com'


@pytest.mark.asyncio
async def test_delete_user(aiohttp_client, setup_database):
    data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

    app = web.Application()
    app.router.add_post('/user/create', create_user)
    app.router.add_get('/user/{id}', get_user)
    app.router.add_delete('/user/{id}', delete_user)
    client = await aiohttp_client(app)

    create_resp = await client.post('/user/create', json=data)
    json_create_resp = await create_resp.json()
    user_id = json_create_resp['id']

    delete_resp = await client.delete(f'/user/{user_id}')
    assert delete_resp.status == 200

    get_resp = await client.get(f'/user/{user_id}')
    assert get_resp.status == 404
    json_resp = await get_resp.json()
    assert json_resp['error'] == 'User with the specified id was not found'


@pytest.mark.asyncio
async def test_list_users(aiohttp_client, setup_database):
    data1 = {'name': 'User 1', 'email': 'user1@example.com', 'password': 'password1'}
    data2 = {'name': 'User 2', 'email': 'user2@example.com', 'password': 'password2'}

    app = web.Application()
    app.router.add_post('/user/create', create_user)
    app.router.add_get('/user/list', list_user)
    client = await aiohttp_client(app)

    await client.post('/user/create', json=data1)
    await client.post('/user/create', json=data2)

    resp = await client.get('/user/list')
    assert resp.status == 200
    json_resp = await resp.json()
    assert len(json_resp) == 2
    assert any(user['name'] == 'User 1' for user in json_resp)
    assert any(user['name'] == 'User 2' for user in json_resp)
