from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    DEFAULT_EMAIL_ADDRESS: EmailStr = "address@domain.com"

    class Config:
        case_sensitive = True


settings = Settings()
