from django.utils import timezone
from memo.models import Child, Prog, Parent

p, cr = Parent.objects.get_or_create(name = "bg")
danni = {
	'db': {'code1': 27, 'code2': 34, 'code3': 29, 'color': "blue", 'mother': p},
	'itn': {'code1': 51, 'code2': 65, 'code3': 27, 'color': "cyan",	'mother': p},
	'pp': {'code1': 0, 'code2': 0, 'code3': 45, 'color': "yellow", 'mother': p},
	'ini': {'code1': 14, 'code2': 13, 'code3': 11, 'color': "green", 'mother': p},
	'bsp': {'code1': 43, 'code2': 36, 'code3': 33, 'color': "red", 'mother': p},
	'dps': {'code1': 30, 'code2': 29, 'code3': 31, 'color': "violet", 'mother': p},
	'gerb': {'code1': 75, 'code2': 63, 'code3': 64, 'color': "black", 'mother': p}}

for da in danni.keys():
	Child.objects.update_or_create(name = da,
								   defaults = danni[da])
p.save()


pp, cr = Parent.objects.get_or_create(name = "prog")
panni = {
	0: {'code1': 1, 'color': "black", 'mother': pp},# unknown
	1: {'code1': 1, 'color': "white", 'mother': pp},# other
	2: {'code1': 61818, 'color': "blue", 'mother': pp},# python
	3: {'code1': 38018, 'color': "red", 'mother': pp},# javascript
	4: {'code1': 65986, 'color': "green", 'mother': pp},# java
	5: {'code1': 27521, 'color': "magenta", 'mother': pp},# c#
	6: {'code1': 36798, 'color': "cyan", 'mother': pp},# c++
	7: {'code1': 3, 'color': "violet", 'mother': pp},# r
	8: {'code1': 3, 'color': "yellow", 'mother': pp},# c
	9: {'code1': 16890, 'color': "orange", 'mother': pp},# php
	10: {'code1': 3, 'color': "brown", 'mother': pp}}# perl

if False: # False to disable update/destroy the database
	# True to enable update/destroy it
	print('warning -> update database')
	for pa in panni.keys():
		Prog.objects.update_or_create(name = pa,
   									  defaults = panni[pa])
	pp.save()
else: print('keep safe database -> edit the script to update')


avec = True
for prog in Prog.objects.all():
	if avec:
		print(prog.mother.name + ' =====================================')
		avec = False
	print(prog.name, prog, prog.code1, prog.color)

avec = True
for child in Child.objects.all():
	if avec:
		print(child.mother.name + ' =====================================')
		avec = False
	print(child.code, child.name, child.color,
		  child.image, child.code1, child.code2, child.code3)





		

