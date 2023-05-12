from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .const import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL: str = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
Base: DeclarativeMeta = declarative_base()

metadata: MetaData = MetaData()

engine: AsyncEngine = create_async_engine(DATABASE_URL, poolclass=NullPool)
async_session_maker: sessionmaker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
