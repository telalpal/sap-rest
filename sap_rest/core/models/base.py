from django.db import models


class SapRestBaseModel(models.Model):
    """
    Common logic for all core models
    """
    class Meta:
        abstract = True
