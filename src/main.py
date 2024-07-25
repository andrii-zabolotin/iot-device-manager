from models import User, Location, Device
from src.api.device import *
from src.api.location import *
from src.api.user import *

app = web.Application()
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
    with db:
        db.create_tables([User, Location, Device], safe=True)


if __name__ == '__main__':
    create_db_tables()
    web.run_app(app, port=8000)
