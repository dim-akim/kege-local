from sqlmodel import SQLModel, Field, JSON

from .models import TaskBase


class File(SQLModel):
    url: str
    name: str
    user_id: str


class SubTask(SQLModel):
    number: int = Field(description='Номер задания ЕГЭ', ge=20, le=21)
    text: str
    key: str
    table: dict = {}


class TaskPublic(TaskBase):
    id: int
    files: list[File]
    sub_task: list[SubTask]


class TaskRead(TaskBase):
    uuid: str = Field(schema_extra={"validation_alias": "id"})
    id: int = Field(schema_extra={"validation_alias": "taskId"})
    hide: bool
    sub_task: list[dict] = Field(schema_extra={"validation_alias": "subTask"})


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    comment: str | None = None
    text: str | None = None
    key: str | None = None
    solve_text: str | None = None
    files: list[File] | None = None
    sub_task: list[SubTask] | None = None
    table: dict | None = None
    difficulty: int | None = None
