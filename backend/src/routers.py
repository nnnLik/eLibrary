from fastapi import APIRouter

from src.user.api import router as user_router


routes = APIRouter()

routes.include_router(
    user_router,
    prefix="/user",
    tags=[
        "user",
    ],
)
