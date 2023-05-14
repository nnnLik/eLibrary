from typing import List

from config.database import get_async_session

from fastapi import APIRouter, Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas import UserRead


router = APIRouter()


@router.get("/users", response_model=List[UserRead])
async def read_users(
    page: int = 1,
    page_size: int = 10,
    session: AsyncSession = Depends(get_async_session),
):
    query = select(User).offset((page - 1) * page_size).limit(page_size)
    result = await session.execute(query)
    users = result.scalars().all()

    return users
