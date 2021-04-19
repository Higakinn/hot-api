from typing import List
from pydantic import BaseModel
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType

class RestaurantModel(BaseModel):
    ids: List[str] = []

class RestaurantGrapheneModel(PydanticObjectType):
    class Meta:
        model = RestaurantModel

class RestaurantGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = RestaurantModel
        # exclude_fields = ('id', )