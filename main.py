from fastapi import FastAPI, Query,Depends, HTTPException, status
from typing import Optional
import secrets
import requests
import os
app = FastAPI(title="api一覧")
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, f"{os.environ['USER']}")
    correct_password = secrets.compare_digest(credentials.password, f"{os.environ['PASS']}")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex='https://.*\.app',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hgs")
def use_hotpepper_gourmet_search_api(
    credentials: HTTPBasicCredentials = Depends(get_current_username),
    lat: float = Query(
        "35.68944",
        title="title",
        description="緯度を入力"
    ),
    lng: float = Query(
        "139.69167",
        title="title",
        description="軽度を入力"
    ),
    range: int = Query(
        "1",
        description="ある地点からの範囲内のお店の検索を行う場合の範囲を5段階で指定できます。たとえば300m以内の検索ならrange=1を指定します 例) 1: 300m 2: 500m 3: 1000m (初期値) 4: 2000m 5: 3000m "
    ),
    order: int = Query(
        "1",
        title="title",
        description="検索結果の並び順を指定します。おススメ順は定期的に更新されます。※ 位置検索の場合、「4:オススメ順」以外は指定に関係なく、強制的に距離順でソートされます。"
    ),
    genre: Optional[str] = Query (
        None,
        description = "お店のジャンル(サブジャンル含む)で絞込むことができます。指定できるコードについてはgenre_master API参照"
    )
    
    ):
    # 34.67  lat
    # lng=135.52
    params = {"lat":lat,"lng":lng,"range":range,"order":order,"genre":genre}
    url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={os.environ['HOT_PEPPAR_API_KEY']}&format=json"
    response = requests.get(url,params)
    # print(response.json())
    return response.json()


@app.get('/genre_master')
def use_genre_master_api(
    credentials: HTTPBasicCredentials = Depends(get_current_username),
    code: Optional[str]= Query(
        None,
        description="ジャンルコードで検索(完全一致)します。（２個まで指定可、3個以上指定すると3個目以降無視します"
    ),
    keyword: Optional[str]= Query(
        None,
        description="ジャンル名で検索(部分一致)します。 UTF8(URLエンコード)で指定"
    )
    ):
        # keyword = base64.encode(keyword)
    params = {"code": code,"keyword": keyword,"format":"json"}
    url = f"http://webservice.recruit.co.jp/hotpepper/genre/v1/?key={os.environ['HOT_PEPPAR_API_KEY']}"
    response = requests.get(url,params)

    return response.json()