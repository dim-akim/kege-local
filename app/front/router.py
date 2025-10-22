from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

from app.front.temp_tasks import temp_task0, temp_kim

router = APIRouter(tags=["Frontend"])

templates = Jinja2Templates(directory="templates")




# class tasks(BaseModel):
#     task_id: int
#     text: str



@router.get("/", response_class=HTMLResponse)
async def get_test(request: Request):
    return templates.TemplateResponse(
        request,
        "test.html",
        context={
            'username': 'donut',
            'task': temp_task0,
        }
    )

@router.get("/variation_table", response_class=HTMLResponse)
async def get_variation_table(request: Request):
    return templates.TemplateResponse(
        "variation_table.html",   # ← укажи расширение!
        {"request": request},
    )


@router.get("/{kim_number}", response_class=HTMLResponse)
async def get_kim(request: Request, kim_number: int):
    return


@router.get("/{kim_number}/answers", response_class=HTMLResponse)
async def get_answer(request: Request, kim_number: int):
    return templates.TemplateResponse(
        request,
        "answe_table.html",
        context={
            'username': 'donut',
            'kim': temp_kim,
            'kim_number': kim_number,
        }
    )


@router.get("/{kim_number}/{task_number}", response_class=HTMLResponse)
async def get_task(request: Request, kim_number: int, task_number: int):
    return templates.TemplateResponse(
        request,
        "test.html",
        # "answe_table.html",
        context={
            'username': 'donut',
            'kim': temp_kim,
            'kim_number': kim_number,
            'task_number': task_number,
        }
    )











