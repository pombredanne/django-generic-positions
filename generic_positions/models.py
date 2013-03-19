"""Models for the ``generic_positions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ObjectPosition(models.Model):
    """
    Model to add a position field to any kind of object.

    :content_object: Object, which now has a position field.
    :position: Current position integer of the object.

    """
    # Generic Foreign Key Bundle
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    # Other fields
    position = models.PositiveIntegerField(verbose_name=_('Position'))

    class Meta:
        ordering = ('position', )


class GenericPositionsModel(models.Model):
    """
    Custom model to sort the queryset with the new position item.

    Therefore we add a position relation on startup.

    """
    class Meta:
        abstract = True

GenericPositionsModel.add_to_class(
    'generic_position', generic.GenericRelation(ObjectPosition))