from typing import List, Optional

from app.dependencies import get_current_username
from app.controller.restaurant import Restaurant
from fastapi import APIRouter, Depends, Query

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
