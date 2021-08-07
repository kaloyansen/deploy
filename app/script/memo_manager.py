from django.utils import timezone
from memo.models import Child, Prog, Parent

""" designed to be run once per deployment
in real /deb = False/ mode """
deb = True
""" should turn deb back to True
after initial tables are created
NOT TESTED read code before run
consider django administration instead """

p = {}
i = 0
bgexiste = False
progexiste = False

for parent in Parent.objects.all():
	pn = parent.name
	print('parent found', pn)
	if pn == "bg": bgexiste = True	
	if pn == "prog": progexiste = True	
	p[i] = parent
	i += 1

lenp = len(p)
print(lenp, 'tables existe')

if deb:
	print('warning: deb = False to create new tables')
	exit(1)
	
if progexiste:
	print('progexiste')
else:
	cc = {}
	pp = Parent(name="prog")
	cc[0] = Prog(name=0, code1=1, color="black", mother=pp)
	cc[1] = Prog(name=1, code1=1, color="white", mother=pp)
	cc[2] = Prog(name=2, code1=14, color="blue", mother=pp)
	cc[3] = Prog(name=3, code1=11, color="red", mother=pp)
	cc[4] = Prog(name=4, code1=7, color="green", mother=pp)
	cc[5] = Prog(name=5, code1=5, color="magenta", mother=pp)
	cc[6] = Prog(name=6, code1=4, color="cyan", mother=pp)
	cc[7] = Prog(name=7, code1=3, color="violet", mother=pp)
	cc[8] = Prog(name=8, code1=3, color="yellow", mother=pp)
	cc[9] = Prog(name=9, code1=6, color="orange", mother=pp)
	cc[10] = Prog(name=10, code1=3, color="brown", mother=pp)

	pp.save()
	for prog in cc.values(): prog.save()

if bgexiste:
	print('bgexiste')
else:
	c = {}
	p = Parent(name="bg")
	c[0] = Child(name='db', code1=27, code2=34, color="blue", mother=p)
	c[1] = Child(name='itn', code1=51, code2=65, color="cyan", mother=p)
	c[2] = Child(name='imv', code1=14, code2=13, color="green", mother=p)
	c[3] = Child(name='bsp', code1=43, code2=36, color="red", mother=p)
	c[4] = Child(name='dps', code1=30, code2=29, color="violet", mother=p)
	c[5] = Child(name='gerb', code1=75, code2=63, color="yellow", mother=p)

	p.save()
	for child in c.values(): child.save()


for child in Child.objects.all():
	parent = child.mother
	print(parent.name,
		  child.code,
		  child.name,
		  child.color,
		  child.image,
		  child.code1,
		  child.code2)

for prog in Prog.objects.all():
	parent = prog.mother
	print(parent.name,
		  prog.name,
		  prog.code1,
		  prog.color)

if deb:
	print('info: tables ok, try deb = True to prevent tables to be created')
	exit(1)

exit(0)



		

