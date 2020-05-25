from enum import Enum

from pydantic import BaseSettings, EmailStr


class EmailService(str, Enum):
    MAILJET = "mailjet"
    SENDGRID = "sendgrid"


class Settings(BaseSettings):
    ENV: str = "dev"
    SENTRY_DSN: str = None
    API_KEY: str = "you-will-want-something-safe-here"
    DEFAULT_EMAIL_ADDRESS: EmailStr = "default@email.com"
    EMAIL_SERVICE: EmailService = EmailService.MAILJET
    SENDGRID_API_KEY: str = "get_your_api_key_from_sendgrid_dashboard"
    MAILJET_API_KEY: str = "get_your_api_key_from_mailjet_dashboard"
    MAILJET_API_SECRET: str = "get_your_api_secret_from_mailjet_dashboard"
    BROKER_URL: str = "amqp://localhost"

    class Config:
        env_file = ".env"
        case_sensitive = True
        fields = {"BROKER_URL": {"env": ["BROKER_URL", "CLOUDAMQP_URL"]}}


settings = Settings()
