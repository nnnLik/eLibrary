from rest_framework import viewsets

from src.base.viewsets import ListCreateViewSet, RetriveUpdateSet
from src.base.paginators import ElibraryCommonPaginator

from .models import BookPublisher, Book, Library, BookAuthor, BookGenre, BookLanguages
from .serializers import (
    BookPublisherSerializer,
    BookSerializer,
    LibrarySerializer,
    BookGenreSerializer,
    BookAuthorSerializer,
    BookLanguageSerializer,
)


class BookPublisherViewSet(ListCreateViewSet):
    queryset = BookPublisher.objects.all()
    serializer_class = BookPublisherSerializer
    pagination_class = ElibraryCommonPaginator


class BookViewSet(RetriveUpdateSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = ElibraryCommonPaginator


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    pagination_class = ElibraryCommonPaginator


class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    pagination_class = ElibraryCommonPaginator


class BookLanguagesViewSet(viewsets.ModelViewSet):
    queryset = BookLanguages.objects.all()
    serializer_class = BookLanguageSerializer
    pagination_class = ElibraryCommonPaginator


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
    pagination_class = ElibraryCommonPaginator
