import sys
from colorama import init, Fore, Back, Style
from pathlib import Path
from work.models import Visitor, Mage

init(autoreset = True)
print(Fore.BLACK + Back.CYAN + '******* {} *******'.format(Path(__file__)))

bouchon = True
timeout = 16 # seconds
visitall = Visitor.objects.all()
visit = visitall.order_by('-date')

def ask_for_y(question = 'y(es) or no?', timeout = 10):
	from select import select
	print(question)
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
		inp_val = sys.stdin.readline()
		inp_val_strip = inp_val.strip()
		if inp_val_strip == 'y':
			print('(+)')
			return True
		else: print('(-) {}'.format(inp_val_strip))		
	else: print('timeout {}'.format(timeout))
	return False


roboco = 0
for v in visit:
	if v.is_robo():	roboco += 1

if roboco == 10: print(Fore.MAGENTA + Back.CYAN + 'no robots')
else:
	print(Fore.MAGENTA + Back.CYAN + '{} robots:'.format(roboco))
	bouchon = not ask_for_y('delete robots y(es)/no?', 16)

mess = 'protection de données '
if bouchon: mess += 'activée'
else: mess += 'déactivée'
# print(mess)

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
