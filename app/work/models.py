from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=44)
    description = models.TextField()
    technology = models.CharField(max_length=120)
    place = models.CharField(max_length=120)
    image = models.FilePathField(path="/img")

