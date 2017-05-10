from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=128, unique=True)
    logo = models.ImageField(upload_to='media/instituteLogo/', blank=False)

    def get_image_path(instance, filename):
        return '/Institute/' + filename

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '%s' % ( self.name)

class School(models.Model):
    name = models.CharField(max_length=128, unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='schools')


    class Meta:
        unique_together = ('institute', 'name')
        ordering = ['name']

    def __unicode__(self):
        return '%s' % ( self.name)

class Department(models.Model):
    name = models.CharField(max_length=128, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')


    class Meta:
        unique_together = ('school', 'name')
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)


class Programme(models.Model):
    TITLES = (
        ('Bridging','Bridging'),
        ('Diploma','Diploma'),
        ('Degree','Degree'),
        ('Masters','Masters'),
        ('Doctorate','Doctorate'),
    )
    name = models.CharField(max_length=128, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programmes')
    title = models.CharField(max_length=128, choices=TITLES)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('department', 'name')
        ordering = ['name']

    def __unicode__(self):
        return '%s' % (self.name)

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

