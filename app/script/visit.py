from work.models import Visitor

visitall = Visitor.objects.all()
visit = visitall.order_by('date')

print ('total ', visit.count())

visifilter = Visitor.objects.filter(voted=True)
print (visifilter.count(), ' voted')
for v in visifilter: print (v)


visifilter = Visitor.objects.exclude(message='')
print (visifilter.count(), ' messages')
for m in visifilter: print (m, '-->', m.message)

robot = visit.filter(voted=False).filter(lang='fr').filter(message='').filter(code__lte=2)
roboco = robot.count()

inpval = 'n'
if roboco == 0:
	print ('no robots')
else:
	inpval = input("delete {} robots (y/n) ? ".format(roboco))
	for v in robot:
		print (v.id, v.date, v.ip_address, v.code, v.voted, v.lang, v.message)
		if inpval == 'y': v.delete()

