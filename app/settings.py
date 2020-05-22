from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    DEFAULT_EMAIL_ADDRESS: EmailStr = "default@email.com"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
