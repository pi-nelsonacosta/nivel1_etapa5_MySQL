from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Añadir aquí la configuración

    azure_openai_api_key: str
    azure_openai_endpoint: str

    class Config:
        env_file = ".env"

settings = Settings()
