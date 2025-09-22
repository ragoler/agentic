from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Defines the application's configuration settings.
    Pydantic will automatically load these from environment variables.
    A .env file can be used for local development.
    """
    APP_NAME: str = "AI Trip Planner"
    GEMINI_API_KEY: str = "YOUR_API_KEY_HERE"

settings = Settings()
