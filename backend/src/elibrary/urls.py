from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import (
    BookPublisherViewSet,
    BookViewSet,
    LibraryViewSet,
    BookGenreViewSet,
    BookAuthorViewSet,
    BookLanguagesViewSet,
)

api_router = DefaultRouter()
api_router.register("book-publisher", BookPublisherViewSet, basename="book-publisher")
api_router.register("book", BookViewSet, basename="book")
api_router.register("library", LibraryViewSet, basename="library")
api_router.register("book-genres", BookGenreViewSet, basename="book-genres")
api_router.register("book-author", BookAuthorViewSet, basename="book-author")
api_router.register("book-language", BookLanguagesViewSet, basename="book-language")

urlpatterns = [
    path("", include(api_router.urls)),
]
