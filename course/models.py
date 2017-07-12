from django.db import models
from programme.models import Programme

class Course(models.Model):



    CHOICES = (
        ('C', 'COMPULSORY'),
        ('E', 'ELECTIVE'),
    )

    code = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    units = models.IntegerField(default=3)
    description = models.TextField(max_length=500)
    year = models.IntegerField()
    semester = models.IntegerField()
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='courses')
    choice = models.CharField(max_length=50, choices=CHOICES)

    class Meta:
        unique_together = ('programme', 'title')
        ordering = ['title']

    def __unicode__(self):
        return '%s' % (self.code)
