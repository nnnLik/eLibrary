import uuid

from django.db import models


class BookPublisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    age_limit = models.PositiveIntegerField()
    publisher = models.ForeignKey(BookPublisher, null=True, on_delete=models.SET_NULL)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"
