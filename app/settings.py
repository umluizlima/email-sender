from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    API_KEY: str = "you-will-want-something-safe-here"
    DEFAULT_EMAIL_ADDRESS: EmailStr = "default@email.com"
    SENDGRID_API_KEY: str = "get_your_api_key_from_sendgrid_dashboard"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
