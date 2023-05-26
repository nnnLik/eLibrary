from django.db import models

from .book import Book


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "genre"


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "language"


class BookLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.book} - Language: {self.language}"

    class Meta:
        db_table = "book_languages"


class BookAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.book} - Author {self.author}"

    class Meta:
        db_table = "book_author"


class BookGenre(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"Book: {self.book} - Genre: {self.genre}"

    class Meta:
        db_table = "book_genre"
