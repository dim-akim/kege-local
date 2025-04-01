from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

# from app.front.router import router as front_router
from app.api import router as api_router


app = FastAPI(
    default_response_class=ORJSONResponse,
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# origins = [
#     "*",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(front_router)
app.include_router(api_router)
