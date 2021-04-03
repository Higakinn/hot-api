import graphene
from typing import List, Optional

from app.dependencies import get_current_username
from app.controller.restaurant import Restaurant
from fastapi import APIRouter, Depends, Query
from app.model.restaurant import RestaurantGrapheneModel, RestaurantModel, RestaurantGrapheneInputModel
router = APIRouter(tags=["restaurant"], dependencies=[Depends(get_current_username)])


@router.post("/restaurant/favorite")
async def add_favorite_restaurant(
    restaurants: Optional[List[str]] = Query(
        None, description="登録したいお気に入りのお店を設定"
    )
):
    # Restaurant().add_favorite()
    return {"test": "test"}


@router.get("/restaurant/favorite")
async def get_favorite_restaurant(
    count: Optional[int] = Query(
        1, description="取得したいお気に入り店舗の数を指定"
    )
):
    return {"test": "test"}

@router.delete("/restaurant/favorite")
async def delete_favorite_restaurant(
    restaurants: Optional[List[str]] = Query(
        None, description="削除したいお店を設定"
    )
):
    return {"test": "test"}


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))
    favorite_restaurant = graphene.Field(RestaurantGrapheneModel, user_id=graphene.String())
    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'

    @staticmethod
    def resolve_favorite_restaurant(parent, info, user_id=None):
        if user_id is None:
            raise graphene.FieldError('user_id is empty')
        # Restaurant().get_favorite(2)
        return Restaurant().get_favorite(2, user_id)

class AddFavorite(graphene.Mutation):
    class Arguments:
        favorite_details = RestaurantGrapheneInputModel()
        user_id = graphene.String()
    
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
        user_id = graphene.String()
    
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