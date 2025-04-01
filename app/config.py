import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        format="%(asctime)s | %(levelname)-7s | %(name)-30s [%(lineno)4d] - %(message)s",
        level=level,
    )


class DatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Settings(DatabaseSettings):
    SECRET_KEY: str
    ALGORITHM: str

    KOMPEGE_API_LINK: str = "https://kompege.ru/api/v1"
    KOMPEGE_TASKS_LINK: str = f"{KOMPEGE_API_LINK}/task/number/"

    EGE_TASK_NUMBERS: list = [i for i in range(1, 28) if i not in (20, 21)]

    model_config = SettingsConfigDict(env_file=".env")


configure_logging(level=logging.DEBUG)
logging.getLogger("python_multipart").setLevel(logging.INFO)
settings = Settings()
