from datetime import datetime
from enum import Enum

from config.database import Base

from fastapi_users_db_sqlalchemy.generics import GUID

from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class BookStatus(str, Enum):
    unread = "unread"
    reading = "reading"
    read = "read"


class Book(Base):
    __tablename__ = "el_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = Column(String(150), nullable=False)
    published_at: Mapped[datetime] = mapped_column(Date(), nullable=False)
    status: Mapped[BookStatus] = Column(String(30), nullable=False)
    library_id: Mapped[int] = Column(Integer, ForeignKey("el_library.id"))

    library = relationship("Library", back_populates="books")
    user_books = relationship("UserBook", back_populates="book")

    def __repr__(self):
        return self.title


class UserBook(Base):
    __tablename__ = "el_user_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: int = Column(Integer, ForeignKey("el_book.id"), nullable=False)
    book: Mapped[Book] = relationship("Book")


class Library(Base):
    __tablename__ = "el_library"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: UUID = Column(GUID, ForeignKey("el_user.id"), nullable=False)
    user_books: int = Column(Integer, ForeignKey("el_user_book.id"), nullable=False)
    user = relationship("User", uselist=False)
    user_books: Mapped[UserBook] = relationship("UserBook")

    def __repr__(self):
        return f"User {self.user_id}"
