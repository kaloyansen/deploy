import random
from django.db import models
from django.utils import timezone



class ColorStyle(models.Model):

	title = models.CharField(max_length = 15)
	
	fr = models.IntegerField(default = 0)
	fg = models.IntegerField(default = 0)
	fb = models.IntegerField(default = 0)
	br = models.IntegerField(default = 0)
	bg = models.IntegerField(default = 0)
	bb = models.IntegerField(default = 0)

	mini = 0
	maxi = 255
	step = 3
		
	def fill(self):

		neuf = False
		if self.fr + self.fg + self. fb + self.br + self.bg + self. bb == 0:
			neuf = True
			
		if neuf:
			self.fr = self.rand_ot_do()
			self.fg = self.rand_ot_do()
			self.fb = self.rand_ot_do()
			self.br = self.rand_ot_do()
			self.bg = self.rand_ot_do()
			self.bb = self.rand_ot_do()
		else:
			self.fr += self.rand_ot_do(-1 * self.step, self.step)
			self.fg += self.rand_ot_do(-1 * self.step, self.step)
			self.fb += self.rand_ot_do(-1 * self.step, self.step)
			self.br += self.rand_ot_do(-1 * self.step, self.step)
			self.bg += self.rand_ot_do(-1 * self.step, self.step)
			self.bb += self.rand_ot_do(-1 * self.step, self.step)
			self.correct_all()
		
	
	def is_not_contrast(self, force = 0.333):

		dirr = abs(self.fr - self.br) / (self.maxi - self.mini)
		digg = abs(self.fg - self.bg) / (self.maxi - self.mini)
		dibb = abs(self.fb - self.bb) / (self.maxi - self.mini)

		if dirr < force: return True
		if digg < force: return True
		if dibb < force: return True
		if dibb + digg + dirr < 3 * force: return True

		return False
	
		
	def rand_ot_do(self, ot = False, do = False):
		mini = self.mini
		maxi = self.maxi
		if ot: mini = ot
		if do: maxi = do
		return random.randint(mini, maxi)


	def correct_all(self):

		self.fr = self.correct(self.fr)
		self.fg = self.correct(self.fg)
		self.fb = self.correct(self.fb)
		self.br = self.correct(self.br)
		self.bg = self.correct(self.bg)
		self.bb = self.correct(self.bb)
		

	def correct(self, x):
		if x > self.maxi: x -= self.maxi
		if x < self.mini: x += self.maxi
		return x


	def __str__(self):
		bgr = 'rgb({}, {}, {})'.format(self.br, self.bg, self.bb)
		fgr = 'rgb({}, {}, {})'.format(self.fr, self.fg, self.fb)
		return 'background-color:{}; color:{};'.format(bgr, fgr)



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
