import requests
from app.settings import settings


class HotPepper:
    def __init__(self):
        self.api_url = settings.HOT_PEPPAR_API_URL

    def gourmet(self, params):
        return self.__request_of("gourmet", params)

    def genre_master(self, params):
        return self.__request_of("genre", params)

    def __request_of(self, api_type="genre",params=None):
        self.api_url = self.api_url.replace("__API_TYPE__", api_type)
        response = requests.get(self.api_url, params)
        return response.json()
