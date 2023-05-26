from rest_framework import serializers

from .models import BookPublisher, Book, Library, BookLanguages, BookAuthor, BookGenre


class BookPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPublisher
        fields = [
            "id",
            "name",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "pages",
            "age_limit",
            "publisher",
            "published_at",
            "created_at",
        ]


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"


class BookLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLanguages
        fields = "__all__"


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = "__all__"


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = "__all__"
