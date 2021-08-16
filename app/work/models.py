from django.db import models
from django.utils import timezone


class ColorStyle(models.Model):
	title = models.CharField(max_length = 15)
	fred = models.IntegerField(default = 0)
	fgre = models.IntegerField(default = 0)
	fblu = models.IntegerField(default = 0)
	bred = models.IntegerField(default = 0)
	bgre = models.IntegerField(default = 0)
	bblu = models.IntegerField(default = 0)

	def __str__(self):
		bg = 'rgb({}, {}, {})'.format(self.bred, self.bgre, self.bblu)
		fg = 'rgb({}, {}, {})'.format(self.fred, self.fgre, self.fblu)
		return 'background-color:{}; color:{};'.format(bg, fg)



class Project(models.Model):
	# index title + slise de description
	title = models.CharField(max_length = 44)
	description = models.TextField(default = 'description', blank = True)
	technology = models.TextField(default = 'technology', blank = True)
	place = models.CharField(max_length = 120)
	image = models.FilePathField(path="/img")

	def __str__(self): return self.title



class Visitor(models.Model):
	ip_address = models.GenericIPAddressField()
	date = models.DateTimeField(default = timezone.now)
	code = models.IntegerField(blank = False,
							   default = 0,
							   verbose_name = 'range')
	voted = models.BooleanField(default = False)
	message = models.TextField(default = '',
							   blank = True,
							   verbose_name = 'message from user')
	lang = models.CharField(default = 'fr',
							max_length = 15,
							verbose_name = 'user language')

	def has_message(self):
		if self.message == '': return False
		return True

	def is_robo(self):
		if self.voted: return False
		if self.lang == 'en': return False
		if self.message != '': return False
		if self.code > 1: return False
		return True

	def __str__(self):
		return "{} {} {} {} {} {} {}".format(self.id,
											 self.date.strftime("%y%m%d"),
											 self.ip_address,
											 self.code,
											 self.voted,
											 self.lang,
											 self.message)



class Page(models.Model):
	name = models.CharField(max_length = 255)
	date = models.DateTimeField(default = timezone.now)
	code = models.IntegerField(blank = False,
							   default = 0,
							   verbose_name = 'range')
	mother = models.ForeignKey(Visitor,
							   default = 1,
							   related_name = 'son',
							   verbose_name = 'visitor',
							   on_delete = models.CASCADE)

	def __str__(self): return self.name
