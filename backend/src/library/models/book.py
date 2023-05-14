from datetime import datetime
from enum import Enum
from uuid import uuid4

from config.database import Base

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class BookStatus(str, Enum):
    unread = 'unread'
    reading = 'reading'
    read = 'read'


class Book(Base):
    __tablename__ = "el_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = Column(String(150), nullable=False)
    published_at: Mapped[datetime] = mapped_column(Date(), nullable=False)
    status: Mapped[BookStatus] = Column(String(30), nullable=False)
    library_id: Mapped[int] = Column(Integer, ForeignKey('el_library.id'))

    library = relationship("Library", back_populates="books")
    user_books = relationship("UserBook", back_populates="book")

    def __repr__(self):
        return self.title


class UserBook(Base):
    __tablename__ = "el_user_book"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    library_id: int = Column(Integer, ForeignKey('el_library.id'), nullable=False)
    book_id: int = Column(Integer, ForeignKey('el_book.id'), nullable=False)


class Library(Base):
    __tablename__ = "el_library"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id = Column('user_id', UUID, ForeignKey('el_user.id'), unique=True, index=True)

    user = relationship("User", back_populates="el_library")
    user_books = relationship("UserBook", back_populates="el_library")

    def __init__(self, user_id: UUID):
        self.id = uuid4()
        self.user_id = user_id

    def __repr__(self):
        return f"User {self.user_id}"
