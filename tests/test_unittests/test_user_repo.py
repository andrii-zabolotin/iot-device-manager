import pytest
from peewee import DoesNotExist

from src.repositories.user import UserRepository


def test_create_user(setup_database):
    data = {'name': 'Test User', 'email': 'testuser@example.com', 'password': 'password123'}
    user = UserRepository(setup_database).create(data)
    assert user.name == 'Test User'
    assert user.email == 'testuser@example.com'
    assert user.password == 'password123'
    assert user.id is not None


def test_get_user(setup_database):
    # Create a user first
    user = UserRepository(setup_database).create({'name': 'Test User', 'email': 'testuser@example.com', 'password': 'password123'})
    # Fetch it using the repository
    fetched_user = UserRepository(setup_database).get(user.id)
    assert fetched_user is not None
    assert fetched_user.name == 'Test User'
    assert fetched_user.email == 'testuser@example.com'
    assert fetched_user.password == 'password123'


def test_update_user(setup_database):
    # Create a user first
    user = UserRepository(setup_database).create({'name': 'Old Name', 'email': 'oldemail@example.com', 'password': 'oldpassword'})
    # Update it
    UserRepository(setup_database).update(user.id, {'name': 'New Name', 'email': 'newemail@example.com', 'password': 'newpassword'})
    updated_user = UserRepository(setup_database).get(user.id)
    assert updated_user is not None
    assert updated_user.name == 'New Name'
    assert updated_user.email == 'newemail@example.com'
    assert updated_user.password == 'newpassword'


def test_delete_user(setup_database):
    user = UserRepository(setup_database).create({'name': 'User to Delete', 'email': 'deletethis@example.com', 'password': 'delete123'})
    UserRepository(setup_database).delete(user.id)
    with pytest.raises(DoesNotExist):
        UserRepository(setup_database).get(user.id)


def test_list_users(setup_database):
    UserRepository(setup_database).create({'name': 'User 1', 'email': 'user1@example.com', 'password': 'password1'})
    UserRepository(setup_database).create({'name': 'User 2', 'email': 'user2@example.com', 'password': 'password2'})
    users = UserRepository(setup_database).list()
    assert len(users) == 2
    assert any(user['name'] == 'User 1' for user in users)
    assert any(user['name'] == 'User 2' for user in users)
