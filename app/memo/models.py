from django.db import models

CHOICE = ((0, 'unknown'),
		  (1, 'other'),
		  (2, 'python'),
		  (3, 'javascript'),
		  (4, 'java'),
		  (5, 'c#'),
		  (6, 'c++'),
		  (7, 'r'),
		  (8, 'c'),
		  (9, 'php'),
		  (10, 'perl'))

dicho = dict(CHOICE)


class Parent(models.Model):
	name = models.CharField(max_length = 31)
	image = models.FilePathField(path = "/img")
	objects = models.Manager()

	def __str__(self): return self.name


class Prog(models.Model):
	name = models.IntegerField(blank = False,
							   default = 2,
							   unique = True,
							   choices = CHOICE,
							   verbose_name = 'option')
	code1 = models.IntegerField(blank = False,
								default = 11,
								verbose_name = 'range')
	color = models.CharField(max_length = 15,
							 default = '',
							 verbose_name = 'color')
	mother = models.ForeignKey(Parent,
							   default = 1,
							   related_name = 'dauthers',
							   on_delete = models.CASCADE)

	def __str__(self): return dicho[self.name]


class Child(models.Model):
	code = models.IntegerField(blank = False,
							   default = 3,
							   verbose_name = 'party code')
	name = models.CharField(max_length = 15,
							default = '',
							verbose_name = 'name')
	color = models.CharField(max_length = 15,
							 default = '',
							 verbose_name = 'color')
	image = models.FilePathField(path="/img")
	code1 = models.IntegerField(default = 11, verbose_name = 'avril2021')
	code2 = models.IntegerField(default = 11, verbose_name = 'juillet2021')
	code3 = models.IntegerField(default = 11, verbose_name = 'novembre2021')
	mother = models.ForeignKey(Parent,
							   related_name = 'children',
							   on_delete = models.CASCADE)

	def __str__(self): return self.name


"""
class Rate(models.Model):
	name = models.CharField(max_length = 15,
							default = 'izobori',
							verbose_name = 'name')
	vote = models.IntegerField(blank = False,
							   default = 0,
							   verbose_name = 'vote')
	mother = models.ForeignKey(Child,
							   related_name = 'children',
							   on_delete = models.CASCADE)
"""
