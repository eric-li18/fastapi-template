<h1 style="text-align:center">⚡ FastAPI Template</h1>
A barebones FastAPI Template repository for creating a backend REST API server.

Several features are included in the template:
- 🖊️ [Poetry](https://python-poetry.org/docs/master/) Dependency Management 
- 🐋 [Docker Compose](https://docs.docker.com/compose/) File
- 🧪 Testing with [Pytest](https://docs.pytest.org/en/6.2.x/) 
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) 

## Run the Application
To run the application in a development environment:
1. Start the database with 
```
docker-compose up
```
2. Navigate to the `backend` directory and install the dependencies and start a python virtual enviornment by running:
```
poetry shell
poetry install
```

3. Start the API server using 
```
uvicorn main:app --reload
```

4. Navigate to `http://localhost:8000/docs` to look through the endpoint documentation!




