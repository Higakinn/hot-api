from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import hotpepper

app = FastAPI(title="api一覧")
app.include_router(hotpepper.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=r"https://.*\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
