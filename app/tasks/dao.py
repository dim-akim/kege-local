from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dao import BaseDAO
from app.db import get_async_session, async_session_maker
from .models import Task
from .schemas import TaskRead


class TaskDAO(BaseDAO):
    model = Task

    @classmethod
    async def add_batch(cls, tasks: list[TaskRead]):
        async with async_session_maker() as session:
            for task in tasks:
                session.add(Task.model_validate(task))
            await session.commit()
