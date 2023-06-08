from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    online = models.URLField(max_length=200, null=True)
    github = models.URLField(max_length=200, null=True)
    technology = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.name