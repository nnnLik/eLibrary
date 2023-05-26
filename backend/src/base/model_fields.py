from typing import Union

from django.db.models import (
    CharField,
    IntegerChoices,
    PositiveSmallIntegerField,
    TextChoices,
)


def get_field_from_choices(
    label, choices_class: Union[IntegerChoices, TextChoices], **kwargs
) -> Union[PositiveSmallIntegerField, CharField]:
    if issubclass(choices_class, IntegerChoices):
        return PositiveSmallIntegerField(label, choices=choices_class.choices, **kwargs)
    elif issubclass(choices_class, TextChoices):
        if "max_length" in kwargs:
            max_length = kwargs.pop("max_length")
        else:
            max_length = max([len(v) for v in choices_class.values])

        return CharField(
            label, choices=choices_class.choices, max_length=max_length, **kwargs
        )
    else:
        raise AssertionError(
            "Unexpected choice class. Must be of IntegerChoices or TextChoices"
        )
