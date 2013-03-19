"""Dummy models to be used in test cases of the ``generic_positions`` app."""
from django.db import models

from ...models import GenericPositionsModel


class DummyModel(GenericPositionsModel):
    """Dummy to be used in test cases of the ``generic_positions`` app."""
    name = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ['generic_position__position']