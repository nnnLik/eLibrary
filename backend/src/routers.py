from fastapi import APIRouter

from src.auth.views import router as user_router


routes = APIRouter()

routes.include_router(
    user_router,
    prefix="/user",
    tags=[
        "user",
    ],
)
