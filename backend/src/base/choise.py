from django.db import models


class BaseTextChoices(models.TextChoices):
    @classmethod
    def max_length(cls):
        return max([len(v) for v in cls.values])
