from django.utils import timezone
from memo.models import Child, Prog, Parent

p, cr = Parent.objects.get_or_create(name = "bg")
danni = {
	'db': {'code1': 27, 'code2': 34, 'code3': 30, 'color': "blue", 'mother': p},
	'itn': {'code1': 51, 'code2': 65, 'code3': 29, 'color': "cyan",	'mother': p},
	'pp': {'code1': 0, 'code2': 0, 'code3': 44, 'color': "yellow", 'mother': p},
	'imv': {'code1': 14, 'code2': 13, 'code3': 0, 'color': "green", 'mother': p},
	'bsp': {'code1': 43, 'code2': 36, 'code3': 47, 'color': "red", 'mother': p},
	'dps': {'code1': 30, 'code2': 29, 'code3': 26, 'color': "violet", 'mother': p},
	'gerb': {'code1': 75, 'code2': 63, 'code3': 64, 'color': "black", 'mother': p}}

for da in danni.keys():
	Child.objects.update_or_create(name = da,
								   defaults = danni[da])
p.save()


pp, cr = Parent.objects.get_or_create(name = "prog")
panni = {
	0: {'code1': 1, 'color': "black", 'mother': pp},
	1: {'code1': 1, 'color': "white", 'mother': pp},
	2: {'code1': 14, 'color': "blue", 'mother': pp},
	3: {'code1': 11, 'color': "red", 'mother': pp},
	4: {'code1': 7, 'color': "green", 'mother': pp},
	5: {'code1': 5, 'color': "magenta", 'mother': pp},
	6: {'code1': 4, 'color': "cyan", 'mother': pp},
	7: {'code1': 3, 'color': "violet", 'mother': pp},
	8: {'code1': 3, 'color': "yellow", 'mother': pp},
	9: {'code1': 6, 'color': "orange", 'mother': pp},
	10: {'code1': 3, 'color': "brown", 'mother': pp}}

if cr:
	for pa in panni.keys():
		Prog.objects.update_or_create(name = pa,
									  defaults = panni[pa])
	pp.save()
else:
	print('not touch prog once created to prevent user data lost')

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





		

