import random
from django.db import models
from django.utils import timezone
from app.encdec import decrypt


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
	step = int(abs(maxi - mini) / 50)
	carr = []
		

	def fill(self):

		neuf = False
		if len(self.carr) == 0:
			self.set_color_array()
			neuf = True
			
		for cname in self.carr:
			nv = 0
			if neuf:
				nv = self.rand_ot_do()
			else:
				nv = self.correct(getattr(self, cname) + self.rand_ot_do(-1 * self.step, self.step))

			setattr(self, cname, nv)

		
	
	def set_color_array(self):
		fi = self._meta.get_fields()
		for f in fi: self.carr.append(f.name)
		self.carr.pop(0) # remove id #
		self.carr.pop(0) # and title #
		

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


class Mage(models.Model):
	name = models.CharField(max_length = 255)
	date = models.DateTimeField(default = timezone.now)
	code = models.IntegerField(blank = False,
							   default = 0,
							   verbose_name = 'range')

	def __str__(self): return self.name


class Visitor(models.Model):
	ip_address = models.GenericIPAddressField()
	date = models.DateTimeField(default = timezone.now)
	code = models.IntegerField(blank = False,
							   default = 0,
							   verbose_name = 'range')
	voted = models.BooleanField(default = False)
	mencrypted = models.BooleanField(default = False)
	message = models.TextField(default = '',
							   blank = True,
							   verbose_name = 'message from user')
	lang = models.CharField(default = 'fr',
							max_length = 15,
							verbose_name = 'user language')
	mages = models.ManyToManyField(Mage,
								   blank = True,
								   related_name = 'mage_visitors')


	def has_message(self):
		if self.message == '': return False
		return True

	def dessage(self):
		if self.mencrypted:	return decrypt(self.message)
		if self.has_message(): return '{} n-e.'.format(self.message)
		return self.message

	def is_robo(self):
		if self.voted: return False
		if self.lang == 'en': return False
		if self.message != '': return False
		if self.marray_size() > 0: return False
		# if self.code > 1: return False
		return True

	def marray_size(self): return len(self.marray())
	def marray(self):
		arr = []
		mag = self.mages.all().order_by('code')
		for m in mag: arr.append(m.name)
		return arr

	def __str__(self):
		return "{} {} {} {} {} {} {}".format(self.id,
											 self.date.strftime("%y%m%d"),
											 self.ip_address,
											 self.code,
											 self.voted,
											 self.lang,
											 self.dessage())


