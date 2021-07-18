from django.db import models
#import datetime
from django.utils import timezone

class Project(models.Model):
	title = models.CharField(max_length=44)
	description = models.TextField()
	technology = models.CharField(max_length=120)
	place = models.CharField(max_length=120)
	image = models.FilePathField(path="/img")

	def __str__(self): return self.title


class Visitor(models.Model):
	ip_address = models.GenericIPAddressField()
	page_visited = models.TextField()
	event_date = models.DateTimeField(default=timezone.now)
	# event_date = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self): return '{}'.format(self.ip_address)
