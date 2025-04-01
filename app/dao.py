import logging

from sqlmodel import SQLModel, select, delete

from app.db import async_session_maker, get_async_session


log = logging.getLogger(__name__)


class BaseDAO:
    model: SQLModel = None

    @classmethod
    async def get_one_by_pk(cls, key):
        async with async_session_maker() as session:
            return await session.get(cls.model, key)

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:

            query = select(cls.model).filter_by(**filter_by)
            # query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.exec(query)
            result = result.one_or_none()
            log.info(f"Query [{cls.model}:{str(filter_by)}] {result = }")

            if result:
                return cls.model.model_validate(result)

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            # __table__.columns убирает лишний уровень вложенности в mappings
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            # result.all() возвращает кортежи с одним элементом - объектом Booking
            #              другие элементы кортежа могут быть дополнительными запрашиваемыми данными из запроса
            # result.scalars().all() возвращает сразу список объектов Booking
            #                        дополнительных данных здесь видно не будет
            return result.mappings().all()

    @classmethod
    async def add(cls, data):
        async with async_session_maker() as session:
            new_entry = cls.model.model_validate(data)
            session.add(new_entry)
            result = await session.commit()
            await session.refresh(new_entry)
            return new_entry

    @classmethod
    async def update(cls, model_id: int, data):
        async with async_session_maker() as session:
            db_model = await session.get(cls.model, model_id)
            if not db_model:
                return None
            update_data = data.model_dump(exclude_unset=True)
            db_model.sqlmodel_update(update_data)
            session.add(db_model)
            await session.commit()
            await session.refresh(db_model)
            return db_model

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                delete(cls.model)
                .filter_by(**filter_by)
                .returning(cls.model.__table__.columns)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
