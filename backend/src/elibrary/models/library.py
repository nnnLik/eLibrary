from django.db import models

from src.core.models import User
from src.base.choise import BaseTextChoices
from src.base.model_fields import get_field_from_choices

from .book import Book


class Library(models.Model):
    class StatusUserBookChoices(BaseTextChoices):
        PROGRESS = "IN PROGRESS", "in progress"
        DONE = "DONE", "done"
        PLANNED = "PLANNED", "planned"

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = get_field_from_choices(
        "Status user book", StatusUserBookChoices, default=StatusUserBookChoices.PLANNED
    )

    def __str__(self):
        return f"Book {self.id} - User {self.user}"

    class Meta:
        db_table = "library"
