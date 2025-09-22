from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Defines the application's configuration settings.
    """
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    APP_NAME: str = "AI Trip Planner"
    GEMINI_API_KEY: str = "YOUR_API_KEY_HERE"

settings = Settings()
