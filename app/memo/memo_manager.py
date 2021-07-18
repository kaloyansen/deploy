from django.utils import timezone
from memo.models import Child, Parent

""" designed to be run once per deployment
in real /deb = False/ mode """
deb = True
""" should turn deb back to True
after initial tables are created
NOT TESTED read code before run
consider django administration instead """

c = {}

p = Parent(name = "bg")

c[0] = Child(name = 'db', code1 = 27, code2 = 35, mother = p)
c[1] = Child(name = 'itn', code1 = 51, code2 = 64, mother = p)
c[2] = Child(name = 'imv', code1 = 14, code2 = 14, mother = p)
c[3] = Child(name = 'bsp', code1 = 43, code2 = 37, mother = p)
c[4] = Child(name = 'dps', code1 = 30, code2 = 30, mother = p)
c[5] = Child(name = 'gerb', code1 = 75, code2 = 61, mother = p)


if deb:
	for child in Child.objects.all():
		parent = child.mother
		print('child', child.name, child.code1, child.code2)
		print('et ce parent', parent.name)	
else:
	p.save()
	for child in c.values(): child.save()
	#p.save()

	for child in c.values():
		parent = child.mother
		print('child', child.name, child.code1, child.code2)
		print('et ce parent', parent.name)	

		
exit(0)



e1 = Europe(pk = 1, title = 'elections bulgares 2021')
e1.save()

for p in pp.values():
	p.save()
	e1.party.add(p)

e1.save()

eu = Europe.objects.all()
for c in eu:
	print('set', c.pk, c.title)
	for ppp in c.party.all():
		print('unit', ppp.pk, ppp.name, ppp.title, ppp.vote1, ppp.vote2)
		if ppp.pk == ppp.name + 1: pass
		else:
			print('oooooooooooooo {} <== {}'.format(ppp.pk, ppp.name + 1))

		

