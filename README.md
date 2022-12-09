# FastAPI Boilerplate
FastAPI REST API pre-configured with a database. This will get you up and running with CRUD operations quickly. Use this starter, boilerplate for all your new FastAPI projects.

## Requirements
- Python3
- python3-virtualenv
- python3-pip

## Features
- SQLAlchemy
- Pydantic

## ToDo
- Docker
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
```

## Quick Start
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

## Contribution

Please submit a pull request for changes you would like to make, with a matching open issue.

Factors that will be considered when new suggestions are proposed:
1. Simple architecture and structure for beginners to understand.
2. Docstring code documentation.
3. FastAPI documention (https://fastapi.tiangolo.com/) guidelines.
