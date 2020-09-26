from typing import Optional

from pydantic import BaseSettings, EmailStr, SecretStr

from .email_service import EmailService
from .environment import Environment


class Settings(BaseSettings):
    ENV: Environment = Environment.DEVELOPMENT
    SENTRY_DSN: SecretStr = None
    API_KEY: SecretStr = "you-will-want-something-safe-here"
    DEFAULT_EMAIL_ADDRESS: EmailStr = "default@email.com"
    EMAIL_SERVICE: EmailService = EmailService.SENDGRID
    SENDGRID_API_KEY: SecretStr = "get_your_api_key_from_sendgrid_dashboard"
    MAILJET_API_KEY: SecretStr = "get_your_api_key_from_mailjet_dashboard"
    MAILJET_API_SECRET: SecretStr = "get_your_api_secret_from_mailjet_dashboard"
    BROKER_URL: str = "amqp://rabbitmq:rabbitmq@localhost"
    BROKER_POOL_LIMIT: Optional[int] = 1
    TEMPLATES_FOLDER: str = "templates"

    class Config:
        env_file = ".env"
        case_sensitive = True
        fields = {"BROKER_URL": {"env": ["BROKER_URL", "CLOUDAMQP_URL"]}}


def get_settings():
    return Settings()
