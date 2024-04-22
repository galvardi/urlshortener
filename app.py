import hashlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import RedirectResponse
from fastapi.responses import RedirectResponse

DOMAIN_NAME = "http://127.0.0.1:8000/"
HASH_SIZE = 10

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

long_to_short_dict = {}
short_to_long_dict = {}


def calculate_hash(st: str) -> str:
    h = hashlib.blake2s(digest_size=4)
    h.update(st.encode())
    return h.hexdigest()
    

# user gives long url receives short
@app.post("/shorten/")
def shorten_url(url: str):
    if url in long_to_short_dict:
        return DOMAIN_NAME + long_to_short_dict[url]

    url_hash = calculate_hash(st=url)

    long_to_short_dict[url] = url_hash
    short_to_long_dict[url_hash] = url

    return DOMAIN_NAME + url_hash


@app.get("/")
async def root():
    return "Landing page!"


# user gives short url gets back long url
@app.get("/{url_hash}")
async def get_long_url(url_hash: str):
    if url_hash not in short_to_long_dict:
        return "URL not found" #change to 404 error

    return RedirectResponse(url=short_to_long_dict[url_hash]) #gal


@app.get("/yahoo")
async def redirect_typer():
    return RedirectResponse(url="https://yahoo.com")