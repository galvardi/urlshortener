from fastapi import FastAPI

from constants import DOMAIN_NAME
from dependencies_container import DependenciesContainer
from utils import calculate_hash

app = FastAPI()
dependencies_container = DependenciesContainer()


@app.get("/test")
async def root():
    return "Working!"


@app.post("/shorten/")
async def shorten_url(url: str):
    hashed_url = calculate_hash(st=url)
    dependencies_container.db.add_url(key=hashed_url, value=url)
    return DOMAIN_NAME + '/' + hashed_url


@app.get("/{url_hash}")
async def get_long_url(hashed_url: str):
    url = dependencies_container.db.get_url(key=hashed_url)
    return url

# TODO: Add initializer
# TODO: Make dynamo functions async using decorator
# TODO: Add exception handling?
# TODO: Add dynamo interface
# TODO: Add logging
# TODO: Add integration test
