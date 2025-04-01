import requests

from app.config import settings


def get_tasks_from_kompege(task_number: int):
    response = requests.get(f'{settings.KOMPEGE_TASKS_LINK}{task_number}')
    return response.json()


if __name__ == '__main__':
    print(get_tasks_from_kompege(19))
