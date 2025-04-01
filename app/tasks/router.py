import logging

from fastapi import APIRouter
from app.tasks import TaskRead, TaskPublic, get_tasks_from_kompege
from app.config import settings
from .dao import TaskDAO


log = logging.getLogger(__name__)

router = APIRouter(
    prefix='/tasks',
    tags=['Задания']
)


@router.get('/pull')
async def pull_all_tasks():
    log.info(f'Pulling all tasks from Kompege.ru')
    result = {"message": "success",
              "detail": {}}
    for number in settings.EGE_TASK_NUMBERS:
        tasks = await pull_task(number)
        await TaskDAO.add_batch(tasks)
        result["detail"][f'Tasks {number}'] = len(tasks)
    return result


@router.get('/pull/{number}', response_model=list[TaskPublic])
async def pull_task(number: int) -> list[TaskRead]:
    tasks_raw = get_tasks_from_kompege(number)

    result = [TaskRead.model_validate(task_dict) for task_dict in tasks_raw]
    log.info(f'Got {len(result)} Tasks #{number} from Kompege.ru')
    return result
