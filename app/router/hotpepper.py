from typing import Optional

from app.dependencies import get_current_username
from app.controller.hotpepper import HotPepper
from fastapi import APIRouter, Depends, Query

router = APIRouter(tags=["hotpepper"], dependencies=[Depends(get_current_username)])


@router.get("/hgs")
async def use_gourmet_search_api(
    lat: float = Query("35.68944", title="title", description="緯度を入力"),
    lng: float = Query("139.69167", title="title", description="軽度を入力"),
    range: int = Query(
        "1",
        description="ある地点からの範囲内のお店の検索を行う場合の範囲を5段階で指定できます。\
                    たとえば300m以内の検索ならrange=1を指定します \
                    例) 1: 300m 2: 500m 3: 1000m(初期値) 4: 2000m 5: 3000m ",
    ),
    order: int = Query(
        "1",
        title="title",
        description="検索結果の並び順を指定します。おススメ順は定期的に更新されます。\
                    ※ 位置検索の場合、「4:オススメ順」以外は指定に関係なく、強制的に距離順でソートされます。",
    ),
    genre: Optional[str] = Query(
        None, description="お店のジャンル(サブジャンル含む)で絞込むことができます。指定できるコードについてはgenre_master API参照"
    ),
    restraurant_id: Optional[str] = Query(
        None, description="お店に割り当てられた番号で検索します。"
    )
):
    # 34.67  lat
    # lng=135.52
    params = {"lat": lat, "lng": lng, "range": range, "order": order, "genre": genre, "id": restraurant_id}
    return HotPepper().gourmet(params)


@router.get("/genre_master")
async def use_genre_master_api(
    code: Optional[str] = Query(
        None, description="ジャンルコードで検索(完全一致)します。（２個まで指定可、3個以上指定すると3個目以降無視します"
    ),
    keyword: Optional[str] = Query(
        None, description="ジャンル名で検索(部分一致)します。 UTF8(URLエンコード)で指定"
    ),
):
    # keyword = base64.encode(keyword)
    params = {"code": code, "keyword": keyword, "format": "json"}

    return HotPepper().genre_master(params)
