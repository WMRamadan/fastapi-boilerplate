<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI image"/>
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

Please submit a pull request for changes you would like to make, with a matching open issue.

Factors that will be considered when new suggestions are proposed:
1. Simple architecture and structure for beginners to understand.
2. Docstring code documentation.
3. FastAPI documention (https://fastapi.tiangolo.com/) guidelines.
4. PEP-8 guidelines (https://peps.python.org/pep-0008/).
