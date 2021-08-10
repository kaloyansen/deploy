from work.models import Visitor

visitall = Visitor.objects.all()
visit = visitall.order_by('-date')

print ('total ', visit.count())

visifilter = Visitor.objects.filter(voted=True)
print ('voted ', visifilter.count())
for v in visifilter: print (v)


visifilter = Visitor.objects.exclude(message='')
print (visifilter.count(), ' messages')
for v in visifilter: print (v.message)

visifilter = Visitor.objects.filter(message='').filter(voted=False)
print (visifilter.count(), ' robots')
for v in visifilter:
	print (v.code)
	#v.delete()


