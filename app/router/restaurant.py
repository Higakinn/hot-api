import graphene
import fastapi
from typing import List, Optional

from app.dependencies import get_current_username
from app.controller.restaurant import Restaurant
from fastapi import APIRouter, Depends, Query, Request
from app.model.restaurant import RestaurantGrapheneModel, RestaurantModel, RestaurantGrapheneInputModel
from fastapi import APIRouter, Depends, Query, Form
from starlette.graphql import GraphQLApp
from app.dependencies import get_current_username


class Query(graphene.ObjectType):
    favorite_restaurant = graphene.Field(
        RestaurantGrapheneModel, 
        user_id = graphene.String(required=True, default_value="testUser", description="ログインユーザIDを指定")
    )

    @staticmethod
    def resolve_favorite_restaurant(parent, info, user_id=None):
        if user_id is None:
            raise graphene.FieldError('user_id is empty')
        # Restaurant().get_favorite(2)
        return Restaurant().get_favorite(user_id)

class AddFavorite(graphene.Mutation):
    class Arguments:
        favorite_details = RestaurantGrapheneInputModel()
        user_id = graphene.String(required=True, default_value="testUser", description="ログインユーザIDを指定")
    
    Output = RestaurantGrapheneModel

    @staticmethod
    def mutate(parent, info, favorite_details, user_id=None):
        if user_id is None:
            raise graphene.FieldError('user_id is empty')
        Restaurant().add_favorite(favorite_details, user_id)
        return RestaurantModel(ids=favorite_details.ids)

class DeleteFavarite(graphene.Mutation):
    class Arguments:
        favorite_details = RestaurantGrapheneInputModel()
        user_id = graphene.String(required=True, default_value="testUser", description="ログインユーザIDを指定")
    
    Output = RestaurantGrapheneModel

    @staticmethod
    def mutate(parent, info, favorite_details, user_id=None):
        if user_id is None:
            raise graphene.FieldError('user_id is empty')

        Restaurant().delete_favorite(favorite_details,user_id)
        # TODO: 削除するものがなくてもRestaurantModelをレスポンスしてしまうのを修正したい
        return RestaurantModel(ids=favorite_details.ids)


class Mutation(graphene.ObjectType):
    add_favorite = AddFavorite.Field()
    delete_favorite = DeleteFavarite.Field()

router = APIRouter(tags=["favorite"], dependencies=[Depends(get_current_username)])
graphql_app = GraphQLApp(schema=graphene.Schema(query=Query,mutation=Mutation))

@router.api_route("/gql", methods=["GET", "POST"])
async def graphql(request: Request,query=fastapi.Query(...)):
    return await graphql_app.handle_graphql(request=request)