import pytest
from peewee import DoesNotExist

from src.repositories.location import LocationRepository


def test_create_location(setup_database):
    data = {'name': 'Test Location'}
    location = LocationRepository(setup_database).create(data)
    assert location.name == 'Test Location'
    assert location.id is not None


def test_get_location(setup_database):
    location = LocationRepository(setup_database).create({'name': 'Test Location'})
    fetched_location = LocationRepository(setup_database).get(location.id)
    assert fetched_location is not None
    assert fetched_location.name == 'Test Location'


def test_update_location(setup_database):
    location = LocationRepository(setup_database).create({'name': 'Old Location'})
    LocationRepository(setup_database).update(location.id, {'name': 'Updated Location'})
    updated_location = LocationRepository(setup_database).get(location.id)
    assert updated_location is not None
    assert updated_location.name == 'Updated Location'


def test_delete_location(setup_database):
    location = LocationRepository(setup_database).create({'name': 'Location to Delete'})
    LocationRepository(setup_database).delete(location.id)
    with pytest.raises(DoesNotExist):
        LocationRepository(setup_database).get(location.id)


def test_list_locations(setup_database):
    LocationRepository(setup_database).create({'name': 'Location 1'})
    LocationRepository(setup_database).create({'name': 'Location 2'})
    locations = LocationRepository(setup_database).list()
    assert len(locations) == 2
    assert any(loc['name'] == 'Location 1' for loc in locations)
    assert any(loc['name'] == 'Location 2' for loc in locations)
