"""TaskFlow configuration settings."""

from os import getenv
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # Application
    app_name: str = "TaskFlow API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Database
    database_url: str = "sqlite:///./taskflow.db"

    # Security
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Pagination
    default_page_size: int = 20
    max_page_size: int = 100


def get_settings() -> Settings:
    """
    Get application settings instance.

    Environment variables take precedence over default values.
    """
    return Settings()


# Global settings instance
settings = get_settings()
