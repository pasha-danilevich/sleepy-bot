from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_PATH = Path(__file__).resolve().parent


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(BASE_PATH, "dev.env"), env_file_encoding="utf-8", extra="ignore"
    )


class BaseTortoiseConnection(Base):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    def get_connection_config(self) -> dict:
        return {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": self.DB_HOST,
                "port": self.DB_PORT,
                "user": self.DB_USER,
                "password": self.DB_PASS,
                "database": self.DB_NAME,
            },
        }


class DefaultDB(BaseTortoiseConnection):
    pass


class Bot(Base):
    BOT_TOKEN: str


class App(Base):
    IS_DEV_MODE: bool = True


class Config(BaseSettings):
    app: App = Field(default_factory=App)
    bot: Bot = Field(default_factory=Bot)  # type: ignore[arg-type]
    default_bd: DefaultDB = Field(default_factory=DefaultDB)  # type: ignore[arg-type]
