import requests
from app.settings import settings


class HotPepper:
    def __init__(self):
        self.api_url = settings.HOT_PEPPAR_API_URL

    def gourmet(self, params):
        return self.__request_of(params, "gourmet")

    def genre_master(self, params):
        return self.__request_of(params, "genre")

    def __request_of(self, params, api_type="genre"):
        self.api_url = self.api_url.replace("__API_TYPE__", api_type)
        response = requests.get(self.api_url, params)
        return response.json()
