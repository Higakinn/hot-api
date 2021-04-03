import graphene
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp

from .router import hotpepper
from .router import restaurant
from .router.restaurant import Query, Mutation

app = FastAPI(title="api一覧")
app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query,mutation=Mutation)))
app.include_router(hotpepper.router)
app.include_router(restaurant.router)
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
