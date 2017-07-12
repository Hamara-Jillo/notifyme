from django.db import models
from school.models import School

class Department(models.Model):
    name = models.CharField(max_length=128, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')


    class Meta:
        unique_together = ('school', 'name')
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)
