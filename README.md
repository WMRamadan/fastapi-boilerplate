# FastAPI Boilerplate
FastAPI REST API pre-configured with a database. This will get you up and running with CRUD operations quickly. Use this starter, boilerplate for all your new FastAPI projects.

## Requirements
- Python3
- python3-virtualenv
- python3-pip
- Docker
- Docker-compose

## Features
- SQLAlchemy
- Pydantic
- Docker

## ToDo
- Celery
- Tests
- Logging

## File Structure
```
.
├── api
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
|   ├── models.py
|   ├── schemas.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── helpers
│       ├── __init__.py
│       └── crud.py
├── docker
│   └── Dockerfile
```

## Quick Start (Local)
1. Clone the repo:
    ```bash
    git clone https://github.com/WMRamadan/fastapi-boilerplate
    cd fastapi-boilerplate
    ```
2. Initialize and activate a virtual environment:
    ```bash
    virtualenv env
    source env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

4. Run the development server:
    ```bash
    uvicorn api.main:app --reload
    ```
5. View the API docs:
    ```bash
    http://localhost:8000/docs
    # OR
    http://localhost:8000/redoc
    ```

## Quick Start (Docker)
1. Clone the repo:
    ```bash
    git clone https://github.com/WMRamadan/fastapi-boilerplate
    cd fastapi-boilerplate
    ```
2. Build:
    ```bash
    docker-compose build
    ```

3. Run the app:
    ```bash
    docker-compose up
    ```

4. View the API docs:
    ```bash
    http://localhost/docs
    # OR
    http://localhost/redoc
    ```

## Linting
You can run `pylint` with the following command inside the `fastapi-boilerplate` directory:
```bash
pylint --recursive=y api
```

## Contribution

Please submit a pull request for changes you would like to make, with a matching open issue.

Factors that will be considered when new suggestions are proposed:
1. Simple architecture and structure for beginners to understand.
2. Docstring code documentation.
3. FastAPI documention (https://fastapi.tiangolo.com/) guidelines.
