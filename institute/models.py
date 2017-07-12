from django.db import models
from images.models import UniversityLogo

class Institute(models.Model):
    name = models.CharField(max_length=128, unique=True)
    logo = models.ForeignKey(UniversityLogo)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)










