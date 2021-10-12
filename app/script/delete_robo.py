import sys
from colorama import init, Fore, Back, Style
from pathlib import Path
from select import select
from work.models import Visitor, Mage

init(autoreset = True)
print(Fore.BLACK + Back.CYAN + '******* {} *******'.format(Path(__file__)))

bouchon = True
timeout = 16 # seconds
visitall = Visitor.objects.all()
visit = visitall.order_by('-date')

roboco = 0
for v in visit:
	if v.is_robo():	roboco += 1

if roboco == 0: print(Fore.MAGENTA + Back.CYAN + 'no robots')
else:
	print(Fore.MAGENTA + Back.CYAN + '{} robots:'.format(roboco))
	if True:
		print('delete robots (y/n) ?',)
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			inp_val = sys.stdin.readline()
			if inp_val.strip() == 'y': bouchon = False
			else: print('négatif'.format(inp_val.strip()))		
		else: print('timeout {}'.format(timeout))
	else: pass

for v in visit:
	v.set_bifi()
	tn = Fore.BLUE + '{} {} '.format(v.ip_address, v.bifistr)
	if v.has_message(): tn += Fore.GREEN + 'message: {} '.format(v.dessage())
	if v.voted: tn += Fore.MAGENTA + 'voted '
	if v.lang == 'en': tn += Fore.CYAN + 'changed language '
	if v.marray_size() > 0: tn += Fore.BLUE + 'marray_size: {}, code: {} '.format(v.marray_size(), v.code)
	if v.is_robo():
		if bouchon: tn += Fore.RED + Back.BLUE + 'to be deleted '
		else:
			v.delete()
			tn += Fore.RED + Back.BLUE + 'deleted '

	print(tn)
