import uuid
from django.db import models

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class UniversityLogo(models.Model):
    image = models.ImageField(upload_to=scramble_uploaded_filename)
    name = models.CharField(max_length=128)

    def __str__(self):

        return self.name
