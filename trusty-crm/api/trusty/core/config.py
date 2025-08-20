from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/trusty"
    )
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    ENV: str = "dev"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
