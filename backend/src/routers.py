from fastapi import APIRouter

from src.auth.auth_config import auth_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead
from src.auth.views import router as user_router


routes = APIRouter()

routes.include_router(
    user_router,
    prefix="/user",
    tags=[
        "user",
    ],
)

routes.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

routes.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
