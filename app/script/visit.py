from pathlib import Path
from colorama import init, Fore, Back, Style
from work.models import Visitor, Mage

init(autoreset = True)
print(Fore.BLACK + Back.CYAN + '******* {} *******'.format(Path(__file__)))

visitall = Visitor.objects.all()

visit = visitall.order_by('-date')
print(Fore.GREEN + 'total {}'.format(visit.count()))

visivote = Visitor.objects.filter(voted=True)
print(Back.BLUE + '\n{} voted'.format(visivote.count()))

for v in visivote: print(v.ip_address)

visimess = Visitor.objects.exclude(message='')
print(Back.MAGENTA + '\n{} messages'.format(visimess.count()))
for v in visimess:
	print('message[{}] = {} {}'.format(v.ip_address,
									v.dessage(),
									len(v.mages.all())))


roboco = 0
for v in visit:
	if v.is_robo(): roboco += 1


inp_val = 'n'
if roboco == 0:
	print(Fore.MAGENTA + Back.CYAN + 'no robots')
else:
	print(Fore.MAGENTA + Back.CYAN + '\nrobots:')
	for v in visit:
		if v.is_robo(): print(v.ip_address, 'size =', v.marray_size())
	inp_val = input(Fore.RED + "delete {} robots (y/n) ? ".format(roboco))
	if inp_val == 'y':
		for v in visit:
			if v.is_robo: v.delete()



def run():
	vv = Visitor.objects.all()
	mm = Mage.objects.all()

	for m in mm:
		danni = []
		for v in vv:
			ipa = v.ip_address
			if m in v.mages.all():
				if ipa == '127.5.0.1': pass
				else: danni.append(ipa)

		if len(danni) > 1: print('{} -> {}'.format(m, danni))







run()



