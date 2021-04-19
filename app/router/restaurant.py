import graphene
from typing import List, Optional

from app.dependencies import get_current_username
from app.controller.restaurant import Restaurant
from fastapi import APIRouter, Depends, Query
from app.model.restaurant import RestaurantGrapheneModel, RestaurantModel, RestaurantGrapheneInputModel

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