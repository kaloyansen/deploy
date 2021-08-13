from work.models import Visitor

visitall = Visitor.objects.all()
visit = visitall.order_by('date')
print('total ', visit.count())

visivote = Visitor.objects.filter(voted=True)
print('\n{} voted'.format(visivote.count())
for v in visivote: print(v)

visimess = Visitor.objects.exclude(message='')
print('\n{} messages'.format(visimess.count())
for m in visimess: print('message[{}] = {}'.format(m.ip_address, m.message))

robot = visit.filter(voted=False).filter(lang='fr').filter(message='').filter(code__lte=2)
roboco = robot.count()

inpval = 'n'
if roboco == 0:
	print('no robots')
else:
	print('\nrobots:')
	for v in robot: print(v)
	inpval = input("delete {} robots (y/n) ? ".format(roboco))
	if inpval == 'y':
		for v in robot:
			v.delete()


