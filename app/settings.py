import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    USER: str = os.getenv("USER", "")
    PASS: str = os.getenv("PASS", "")
    HOT_PEPPAR_API_URL: str = f"http://webservice.recruit.co.jp/hotpepper/__API_TYPE__/v1/ \
                                ?key={os.environ['HOT_PEPPAR_API_KEY']}&format=json"
    FIREBASE_PROJECT_ID: str = os.getenv('FIREBASE_PROJECT_ID', '')
    GOOGLE_APP_CREDENTIALS: str = "/app/app/service_account.json"

settings = Settings()
