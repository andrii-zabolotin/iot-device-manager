import pytest
from peewee import DoesNotExist

from src.repositories.device import DeviceRepository


def test_create_device(setup_database, get_location, get_user):
    data = {
        'name': 'Test Device',
        'type': 'Type A',
        'login': 'device_login',
        'password': 'device_password',
        'location': get_location,
        'user': get_user
    }
    device = DeviceRepository(setup_database).create(data)
    assert device.name == 'Test Device'
    assert device.type == 'Type A'
    assert device.login == 'device_login'
    assert device.password == 'device_password'
    assert device.location == get_location
    assert device.user == get_user
    assert device.id is not None


def test_get_device(setup_database, get_location, get_user):
    device = DeviceRepository(setup_database).create({
        'name': 'Test Device',
        'type': 'Type A',
        'login': 'device_login',
        'password': 'device_password',
        'location': get_location,
        'user': get_user
    })
    fetched_device = DeviceRepository(setup_database).get(device.id)
    assert fetched_device is not None
    assert fetched_device.name == 'Test Device'
    assert fetched_device.type == 'Type A'
    assert fetched_device.login == 'device_login'
    assert fetched_device.password == 'device_password'
    assert fetched_device.location == get_location
    assert fetched_device.user == get_user


def test_update_device(setup_database, get_location, get_user):
    device = DeviceRepository(setup_database).create({
        'name': 'Old Device',
        'type': 'Type B',
        'login': 'old_login',
        'password': 'old_password',
        'location': get_location,
        'user': get_user
    })
    DeviceRepository(setup_database).update(device.id, {
        'name': 'Updated Device',
        'type': 'Type C',
        'login': 'new_login',
        'password': 'new_password'
    })
    updated_device = DeviceRepository(setup_database).get(device.id)
    assert updated_device is not None
    assert updated_device.name == 'Updated Device'
    assert updated_device.type == 'Type C'
    assert updated_device.login == 'new_login'
    assert updated_device.password == 'new_password'


def test_delete_device(setup_database, get_location, get_user):
    device = DeviceRepository(setup_database).create({
        'name': 'Device to Delete',
        'type': 'Type D',
        'login': 'delete_login',
        'password': 'delete_password',
        'location': get_location,
        'user': get_user
    })
    DeviceRepository(setup_database).delete(device.id)
    with pytest.raises(DoesNotExist):
        DeviceRepository(setup_database).get(device.id)


def test_list_devices(setup_database, get_location, get_user):
    DeviceRepository(setup_database).create({
        'name': 'Device 1',
        'type': 'Type E',
        'login': 'login1',
        'password': 'password1',
        'location': get_location,
        'user': get_user
    })
    DeviceRepository(setup_database).create({
        'name': 'Device 2',
        'type': 'Type F',
        'login': 'login2',
        'password': 'password2',
        'location': get_location,
        'user': get_user
    })
    devices = DeviceRepository(setup_database).list()
    assert len(devices) == 2
    assert any(device['name'] == 'Device 1' for device in devices)
    assert any(device['name'] == 'Device 2' for device in devices)


def test_get_device_invalid_id(setup_database):
    repository = DeviceRepository(setup_database)
    with pytest.raises(DoesNotExist):
        repository.get(-1)


def test_update_device_invalid_id(setup_database):
    repository = DeviceRepository(setup_database)
    with pytest.raises(DoesNotExist):
        repository.update(-1, {
            'name': 'Nonexistent Device',
            'type': 'Type X',
            'login': 'invalid_login',
            'password': 'invalid_password'
        })


def test_delete_device_invalid_id(setup_database):
    repository = DeviceRepository(setup_database)
    with pytest.raises(DoesNotExist):
        repository.delete(-1)
