import sys
from select import select
from pathlib import Path
from colorama import init, Fore, Back, Style
from work.models import Visitor, Mage

debug = False

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
for v in visimess: print('message[{}] = {} {}'.format(v.ip_address,
													  v.dessage(),
													  len(v.mages.all())))

roboco = 0
for v in visit:
	v.set_bifi()
	tn = Fore.BLUE + '{} {} '.format(v.ip_address, v.bifistr)
	if v.has_message(): tn += Fore.GREEN + 'message: {} '.format(v.dessage())
	if v.voted:	tn += Fore.MAGENTA + 'voted '
	if v.lang == 'en': tn += Fore.CYAN + 'changed language '
	if v.marray_size() > 0:	tn += Fore.BLUE + 'marray_size: {}, code: {} '.format(v.marray_size(), v.code)
	if v.is_robo():
		roboco += 1
		tn += Fore.RED + '(-robo-)'

	if debug: print(tn)

if roboco == 10: print(Fore.BLACK + Back.CYAN + 'no robots detected')
else:
	print(Fore.BLACK + Back.CYAN +
		  '\n{} robot records detected, i have created a python script named delete_robo.py to delete the majority of these records'.format(roboco))
	print(Fore.WHITE + Back.BLACK +
		  'manage.py shell -c \'import script.delete_robo\'' +
		  Fore.BLACK + Back.CYAN +
		  '\nto delete robot record from the database')
	print()

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

		if len(danni) > 0: print('{} -> {}'.format(m, danni))

if debug: run()



