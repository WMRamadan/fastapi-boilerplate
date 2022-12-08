# FastAPI Boilerplate
FastAPI REST API pre-configured with a database. This will get you up and running with CRUD operations quickly. Use this starter, boilerplate for all your new FastAPI projects.

## Requirements
- Python3
- python3-virtualenv
- python3-pip

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
