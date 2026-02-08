"""
Configuración de la aplicación - TaskFlow
Unidad: 3.1 - Introducción a FastAPI
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración de la aplicación."""

    # API
    APP_NAME: str = "TaskFlow API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql://taskflow:taskflow@localhost:5432/taskflow"

    # Security
    SECRET_KEY: str = "tu-secret-key-aqui-cambialo-en-produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
