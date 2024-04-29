from fastapi import FastAPI, Body, Response
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from constants import DOMAIN_NAME
from dependencies_container import DependenciesContainer
from utils import calculate_hash

app = FastAPI(root_path="/api")
# app = FastAPI()
dependencies_container = DependenciesContainer()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add a log for all incoming requests
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response


# @app.get("/api/test")
@app.get("/test")
async def root():
    return "Working!"


@app.post("/shorten")
async def shorten_url(payload: dict = Body(..., json=True)):
    url = payload['url']
    hashed_url = calculate_hash(st=url)
    dependencies_container.db.add_url(key=hashed_url, value=url)
    # return DOMAIN_NAME + '/' + hashed_url
    return {'shortenedURL':DOMAIN_NAME + '/' + hashed_url}

@app.get("/{hashed_url}")
async def get_long_url(hashed_url: str):
    url = dependencies_container.db.get_url(key=hashed_url)
    return RedirectResponse("https://" + url, status_code=302)
 # todo check fix parsing


# TODO: Make dynamo functions async using decorator
# TODO: Add exception handling?
# TODO: Add dynamo interface
# TODO: Add logging
# TODO: Add integration test
