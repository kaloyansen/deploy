from colorama import init, Fore, Back, Style
from work.models import Visitor

init(autoreset = True)

visitall = Visitor.objects.all()
visit = visitall.order_by('date')
print(Fore.GREEN + 'total {}'.format(visit.count()))

visivote = Visitor.objects.filter(voted=True)
print(Back.BLUE + '\n{} voted'.format(visivote.count()))
for v in visivote: print(v)

visimess = Visitor.objects.exclude(message='')
print(Back.MAGENTA + '\n{} messages'.format(visimess.count()))
for v in visimess: print('message[{}] = {}'.format(v.ip_address, v.message))

robot = visit.filter(voted=False).filter(lang='fr').filter(message='').filter(code__lte=2)
roboco = robot.count()

inpval = 'n'
if roboco == 0:
	print('no robots')
else:
	print(Fore.MAGENTA + Back.CYAN + '\nrobots:')
	for v in robot: print(v)
	inpval = input(Fore.RED + "delete {} robots (y/n) ? ".format(roboco))
	if inpval == 'y':
		for v in robot:
			v.delete()


