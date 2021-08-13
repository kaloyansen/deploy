from work.models import Visitor

visitall = Visitor.objects.all()
visit = visitall.order_by('date')
print ('total ', visit.count())

visivote = Visitor.objects.filter(voted=True)
print (visivote.count(), ' voted')
for v in visivote: print (v)

visimess = Visitor.objects.exclude(message='')
print (visimess.count(), ' messages')
for m in visimess: print('message[{}] = {}'.format(m.ip_address, m.message))

robot = visit.filter(voted=False).filter(lang='fr').filter(message='').filter(code__lte=2)
roboco = robot.count()

inpval = 'n'
if roboco == 0:
	print ('no robots')
else:
	inpval = input("delete {} robots (y/n) ? ".format(roboco))
	for v in robot:
		print (v)
		if inpval == 'y': v.delete()

