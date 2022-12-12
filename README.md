<p align="center">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI image"/>
</p>
<p align="center">
    <a href="https://github.com/WMRamadan/fastapi-boilerplate/actions/workflows/python-app.yml" target="_blank">
    <img src="https://github.com/wmramadan/fastapi-boilerplate/actions/workflows/python-app.yml/badge.svg" alt="Test">
    </a>
    <img src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue" alt="Supported Python versions">
</p>

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
- Logging
- Celery
- Tests
- Config

## ToDo
- Run Celery Worker in Docker

## File Structure
```
.
├── api
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
|   ├── worker.py
│   └── models
│   │   ├── __init__.py
│   │   ├── item_model.py
│   │   └── task_model.py
│   │   └── user_model.py
│   └── schemas
│   │   ├── __init__.py
│   │   ├── items_schema.py
│   │   └── tasks_schema.py
│   │   └── users_schema.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── async_router.py
│   │   ├── items.py
│   │   ├── tasks.py
│   │   └── users.py
│   └── helpers
│   │   ├── __init__.py
│   │   ├── async_helper.py
│   │   └── crud.py
│   └── tests
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── test_main.py
├── docker
│   └── Dockerfile
```

## Environment Variables
- SQLALCHEMY_DATABASE_URL - Database URL used, can be either SQLite or PostgreSQL.
- CELERY_CONF_BROKER_URL - Celery redis broker URL.
- CELERY_CONF_RESULT_BACKEND - Celery redis result backend.
- ALLOWED_ORIGINS - A list of origins that should be permitted to make cross-origin requests.
- ALLOW_CREDENTIALS - Allowed credentials `bool` for CORS middelware.
- ALLOW_METHODS - Allowed methods ['GET','POST','PUT','PATCH','DELETE','OPTIONS'] for CORS middleware.
- ALLOW_HEADERS - A list of HTTP request headers that should be supported for cross-origin requests.
- APP_DEBUG - Set app debug mode `bool` value.

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

4. Run `redis` service required for celery worker:
    ```bash
    docker-compose -f docker-compose-services.yml up -d
    ```

5. Run `celery` worker:
    ```bash
    celery --app=api.worker.celery worker --loglevel=info --logfile=celery.log
    ```

6. Run the development server:
    ```bash
    uvicorn api.main:app --reload
    ```

7. View the API docs:
    ```bash
    http://localhost:8000/docs
    # OR
    http://localhost:8000/redoc
    ```

## Linting
You can run `pylint` with the following command inside the `fastapi-boilerplate` directory:
```bash
pylint --recursive=y api
```

## Running Tests
You can run `pytest` with the following command inside the `fastapi-boilerplate` directory:
```bash
pytest api/
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

## Contribution

Please check our [Contributing Guide](./CONTRIBUTING.md) on how you can contribute.
