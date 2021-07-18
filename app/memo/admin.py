from django.contrib import admin
from .models import Langage, Child, Parent, Coder, Prog

class ProgInline(admin.TabularInline): model = Prog	
class CoderAdmin(admin.ModelAdmin):	inlines = [ ProgInline ]	
class ChildInline(admin.TabularInline):	model = Child	
class ParentAdmin(admin.ModelAdmin): inlines = [ ChildInline ]	
class ChildAdmin(admin.ModelAdmin):	pass
class LangageAdmin(admin.ModelAdmin): pass
class ProgAdmin(admin.ModelAdmin): pass

admin.site.register(Langage, LangageAdmin)
admin.site.register(Coder, CoderAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Prog, ProgAdmin)

