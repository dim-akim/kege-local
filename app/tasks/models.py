from datetime import datetime

from sqlmodel import SQLModel, Field, JSON, Column, func, TIMESTAMP

from app.db import Base


class TaskBase(SQLModel):
    number: int = Field(description='Номер задания ЕГЭ', ge=1, le=27)
    comment: str
    text: str
    key: str
    solve_text: str
    files: list[dict] = Field(sa_column=Column(JSON))
    sub_task: list[dict] = Field(sa_column=Column(JSON))
    table: dict = Field(sa_column=Column(JSON))
    difficulty: int


class Task(Base, TaskBase, table=True):
    created_at: datetime = Field(default=None,
                                 sa_column=Column(TIMESTAMP(timezone=True)))
    updated_at: datetime = Field(default=None,
                                 sa_column=Column(TIMESTAMP(timezone=True)))
    pulled_at: datetime = Field(default=None,
                                sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()))
