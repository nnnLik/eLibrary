import uuid

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.generics import GUID

from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.config.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "el_user"

    id = mapped_column(GUID, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = Column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=320),
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    # library = relationship("Library", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User: {self.username}>"
