from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """Time Stamp Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True