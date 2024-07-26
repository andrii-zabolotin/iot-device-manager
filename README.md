# IoT-device-manager
Application for management IoT devices on Python.

## Installation
1. Clone repository
    ```bash 
    git clone https://github.com/0xf0r3v3r/iot-device-manager.git
    ```
2. Change directory
    ```bash
    cd iot-device-manager
    ```
3. Build docker images
    ```bash
    docker-compose build
    ```
## Run

Run all services
```bash
docker-compose up
```
   
## To run Tests
```bash
docker-compose -f docker-compose.test.yml up
```

## API Documentation
### User
#### Create User
- **Method**: POST
- **URL**: `/user/create`
- **Description**: Creates a new user.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
  
#### List of Users
- **Method**: GET
- **URL**: `/user/list`
- **Description**: Retrieves a list of all users.
- **Request body**: No request body required.

#### Get User by ID
- **Method**: GET
- **URL**: `/user/{id}`
- **Description**: Retrieves a user by their ID.
- **Path Parameters**:
  - **id**: The ID of the user to retrieve. (Example: `1`)
- **Request body**: No request body required.

#### Update User
- **Method**: PATCH
- **URL**: `/user/{id}`
- **Description**: Updates an existing user by their ID.
- **Path Parameters**:
  - **id**: The ID of the user to be updated.
- **Request Body**:
  ```json
  {
    "name": "John Smith",
  }
  ```
#### Delete User
- **Method**: DELETE
- **URL**: `/user/{id}`
- **Description**: Deletes a user by their ID.
- **Path Parameters**:
  - **id**: The ID of the user to be deleted.

### Device
#### Create Device
- **Method**: POST
- **URL**: `/device/create`
- **Description**: Creates a new device.
- **Request Body**:
  ```json
  {
    "name": "Device1",
    "type": "sensor",
    "login": "room1",
    "password": "room1",
    "location": 1,
    "user": 2
  }
  ```
#### List of Devices
- **Method**: GET
- **URL**: `/device/list`
- **Description**: Retrieves a list of all devices.
- **Request body**: No request body required.
#### Get Device by ID
- **Method**: GET
- **URL**: `/device/{id}`
- **Description**: Retrieves a device by its ID.
- **Path Parameters**:
  - **id**: The ID of the device to retrieve (integer).
- **Request body**: No request body required.
#### Update Device 
- **Method**: PATCH
- **URL**: `/device/{id}`
- **Description**: Updates an existing device by its ID.
- **Path Parameters**:
  - **id**: The ID of the device to be updated.
- **Request Body**:
  ```json
  {
    "name": "UpdatedDevice"
  }
  ```
#### Delete Device
- **Method**: DELETE
- **URL**: `/device/{id}`
- **Description**: Deletes a device by its ID.
- **Path Parameters**:
  - **id**: The ID of the device to be deleted (integer).
- **Request body**: No request body required.
### Location
#### Create Location
- **Method**: POST
- **URL**: `/location/create`
- **Description**: Creates a new location.
- **Request Body**:
  ```json
  {
    "name": "Room1"
  }
  ```
#### List of Locations
- **Method**: GET
- **URL**: `/location/list`
- **Description**: Retrieves a list of all locations.
- **Request body**: No request body required.
#### Get Location by ID
- **Method**: GET
- **URL**: `/location/{id}`
- **Description**: Retrieves a location by its ID.
- **Path Parameters**:
  - **id**: The ID of the location to retrieve. 
- **Request body**: No request body required.
#### Update Location
- **Method**: PATCH
- **URL**: `/location/{id}`
- **Description**: Updates an existing location by its ID.
- **Path Parameters**:
  - **id**: The ID of the location to be updated.
- **Request Body**:
  ```json
  {
    "name": "Updated Location Name"
  }
  ```
#### Delete Location
- **Method**: DELETE
- **URL**: `/location/{id}`
- **Description**: Deletes a location by its ID.
- **Path Parameters**:
  - **id**: The ID of the location to delete.
- **Request body**: No request body required.

### Built with
<ul>
    <li>Python</li>
    <li>aiohttp</li>
    <li>peewee</li>
    <li>pytest </li>
    <li>Docker</li>
    <li>PostgreSQL</li>
</ul>    
