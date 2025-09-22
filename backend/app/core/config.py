from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Trip Planner"
    GEMINI_API_KEY: str = "YOUR_API_KEY_HERE"

    class Config:
        env_file = ".env"

settings = Settings()
