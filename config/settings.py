from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Projet Instit Watch"
    app_env: str = "development"
    timezone: str = "Europe/Paris"

    openai_api_key: str | None = None
    openai_model: str = "gpt-5"
    openai_temperature: float = 0

    fred_api_key: str | None = None
    alpha_vantage_api_key: str | None = None

    email_from: str | None = None
    email_to: str | None = None

    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_user: str | None = None
    smtp_password: str | None = None

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()