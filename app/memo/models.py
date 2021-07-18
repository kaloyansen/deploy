from django.db import models

CHOICE = ((0, 'unknown'),
		  (1, 'javascript'),
		  (2, 'c++'),
		  (3, 'perl'),
		  (4, 'c#'),
		  (5, 'java'),
		  (6, 'php'),
		  (7, 'c'),
		  (8, 'r'),
		  (9, 'python'),
		  (10, 'other'))

ELEBG = ((0, 'gerb'),
		 (1, 'db'),
		 (2, 'itn'),
		 (3, 'bsp'),
		 (4, 'dps'),
		 (5, 'fachaux'),
		 (6, 'c'),
		 (7, 'imv'))


class CoderManager(models.Manager):
	# Enable fixtures using self.name instead of `id`
	def get_by_natural_key(self, name):
		return self.get(name=name)


class Coder(models.Model):
	objects = CoderManager()
	name = models.CharField(max_length = 31)
	image = models.FilePathField(path = "/img")
	objects = models.Manager()
	
	def __unicode__(self): return u'%s' % self.name


class Prog(models.Model):
	name = models.IntegerField(blank = False,
							   default = 2,
							   choices = CHOICE,
							   verbose_name = "programming language")
	code = models.IntegerField(blank = False,
							   default = 11,
							   verbose_name = 'langage range')
	father = models.ForeignKey("Coder",
							   default = 1,
							   related_name = 'papa',
							   on_delete = models.CASCADE)
	
	def __str__(self): return CHOICE[self.name]


class Langage(models.Model):
	name = models.IntegerField(blank = False,
							   default = 3,
							   # unique = False,
							   choices = CHOICE,
							   verbose_name = "programming language")

	def __str__(self): return CHOICE[self.name]


class Parent(models.Model):
	name = models.CharField(max_length = 31)
	image = models.FilePathField(path = "/img")
	objects = models.Manager()
	
	def __str__(self): return self.name


class Child(models.Model):
	code = models.IntegerField(blank = False,
							   default = 3,
							   #choices = ELEBG,
							   verbose_name = 'party code')
	name = models.CharField(max_length = 15,
							default = '',
							verbose_name = 'name')
	color = models.CharField(max_length = 15,
							default = '',
							verbose_name = 'color')
	image = models.FilePathField(path="/img")
	code1 = models.IntegerField(default = 11,
								verbose_name = 'avril2021')
	code2 = models.IntegerField(default = 11,
								verbose_name = 'juillet2021')
	mother = models.ForeignKey(Parent,
							   related_name = 'children',
							   on_delete = models.CASCADE)

	def __str__(self): return self.name
