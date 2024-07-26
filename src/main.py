import logging

from src.models import User, Location, Device
from src.api.device import *
from src.api.location import *
from src.api.user import *

# logger configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

# create a new aiohttp web application instance.
app = web.Application()

# set up the HTTP routes
app.router.add_post('/user/create', create_user)
app.router.add_get('/user/list', list_user)
app.router.add_get('/user/{id}', get_user)
app.router.add_patch('/user/{id}', update_user)
app.router.add_delete('/user/{id}', delete_user)

app.router.add_post('/device/create', create_device)
app.router.add_get('/device/list', list_device)
app.router.add_get('/device/{id}', get_device)
app.router.add_patch('/device/{id}', update_device)
app.router.add_delete('/device/{id}', delete_device)

app.router.add_post('/location/create', create_location)
app.router.add_get('/location/list', list_location)
app.router.add_get('/location/{id}', get_location)
app.router.add_patch('/location/{id}', update_location)
app.router.add_delete('/location/{id}', delete_location)


def create_db_tables():
    """
    Creates the database tables for the User, Location, and Device models.
    """
    with db:
        db.create_tables([User, Location, Device], safe=True)


if __name__ == '__main__':
    create_db_tables()
    web.run_app(app, port=8000, access_log_format='%a %t "%r" %s "%{Referer}i" "%{User-Agent}i"')
