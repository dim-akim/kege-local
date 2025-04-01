from fastapi import APIRouter
# from fastapi_users import FastAPIUsers
#
# from app.users.auth.base_config import auth_backend
# from app.users.auth.manager import get_user_manager
# from app.users.auth.models import User
# from app.users.auth.schemas import UserRead, UserCreate
# from app.users.profile.router import router as profile_router
from app.tasks import router as tasks_router


router = APIRouter(
    prefix="/api"
)

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )


# router.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )
#
# router.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )

# router.include_router(profile_router)
router.include_router(tasks_router)
