from django.contrib import admin

from .models import (
    Book,
    BookPublisher,
    Library,
    Genre,
    Author,
    Language,
    BookGenre,
    BookAuthor,
    BookLanguages,
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "pages",
        "age_limit",
        "publisher",
        "published_at",
        "created_at",
    ]
    list_filter = ["age_limit", "publisher"]


@admin.register(BookPublisher)
class BookPublisherAdmin(admin.ModelAdmin):
    list_filter = ["name"]


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "book",
        "user",
        "status",
    ]
    list_display = ["user", "book", "status"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(BookLanguages)
class BookLanguagesAdmin(admin.ModelAdmin):
    pass


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    pass
