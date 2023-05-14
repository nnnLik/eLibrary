from fastapi import APIRouter, Depends

from config.database import get_async_session

from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.schemas import UserList

router = APIRouter()


@router.get("/", response_model=UserList)
async def get_users(db: Session = Depends(get_async_session)) -> UserList:
    query = User.__table__.select()
    result = await db.fetch_all(query)
    return {"users": result}
