from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    database_uri: str = "sqlite+aiosqlite://"


settings = Settings()
