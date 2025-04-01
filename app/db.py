from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declared_attr
from sqlmodel import SQLModel, Field, TIMESTAMP, func
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config import settings


engine = create_async_engine(settings.db_url, echo=True, future=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(SQLModel):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=None,
                                 sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(default=None,
                                 sa_column_kwargs={"server_default": func.now(),
                                                   "onupdate": func.now()})
    is_deleted: bool = Field(default=False)


class BaseUpdate(SQLModel):

    is_deleted: bool | None = None


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
