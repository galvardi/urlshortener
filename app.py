from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from constants import DOMAIN_NAME, HTTP, HTTPS
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

class Item(BaseModel):
    url:str


# Add a log for all incoming requests
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response


# @app.get("/api/test")
@app.get("/test")
async def root():
    return "Working as planned!"

# hashing the original url and adding to db
@app.post("/shorten")
async def shorten_url(payload: Item):
    url = payload.url
    hashed_url = calculate_hash(st=url)
    dependencies_container.db.add_url(key=hashed_url, value=url)
    return {'shortenedURL':DOMAIN_NAME + '/api/' + hashed_url}

# gets original url from db and redirecting to it
@app.get("/{hashed_url}")
async def get_long_url(hashed_url: str):
    url = dependencies_container.db.get_url(key=hashed_url)
    if not url: return RedirectResponse(DOMAIN_NAME, status_code=404)
    if not (url[:8] == HTTPS or url[:7] == HTTP):
        url = HTTPS + url
    return RedirectResponse(url=url)