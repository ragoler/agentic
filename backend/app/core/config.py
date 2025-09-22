from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Trip Planner"

    class Config:
        env_file = ".env"

settings = Settings()
