from __future__ import unicode_literals #Support Python2
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible #Support Python2
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title