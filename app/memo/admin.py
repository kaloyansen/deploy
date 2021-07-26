from django.contrib import admin
from .models import Child, Parent, Prog

class ProgAdmin(admin.ModelAdmin): pass
class ProgInline(admin.TabularInline): model = Prog	
class ChildAdmin(admin.ModelAdmin):	pass
class ChildInline(admin.TabularInline):	model = Child	
class ParentAdmin(admin.ModelAdmin): inlines = [ ChildInline, ProgInline ]	

admin.site.register(Child, ChildAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Prog, ProgAdmin)

