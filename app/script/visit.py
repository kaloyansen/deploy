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

if roboco == 0: print(Fore.MAGENTA + Back.CYAN + 'no robots')
else: print(Fore.MAGENTA + Back.CYAN + '{} robots:'.format(roboco))
for v in visit:
	if v.is_robo():
		inp_val = input(Fore.RED + '{} {} delete robot (y/n) ? '.format(v, v.marray_size()))
		if inp_val == 'y': v.delete()
	elif v.has_message():
		print(Fore.RED + '{} {}'.format(v, v.dessage()))
	elif v.voted:
		print(Fore.RED + '{} voted'.format(v))
	elif v.lang == 'en':
		print(Fore.RED + '{} language {}'.format(v, v.lang))
	elif v.lang == 'en':
		print(Fore.RED + '{} language {}'.format(v, v.lang))
	else:
		print(Fore.RED + '{} error'.format(v))




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



