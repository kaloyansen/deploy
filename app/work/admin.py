from django.contrib import admin
from django.db import models
from work.models import Project, Visitor, Mage, ColorStyle

class MageAdmin(admin.ModelAdmin): pass
# class MageInline(admin.TabularInline): model = Mage
class VisitorAdmin(admin.ModelAdmin): pass #inlines = [ MageInline ]
class ProjectAdmin(admin.ModelAdmin): pass
class ColorStyleAdmin(admin.ModelAdmin): pass

admin.site.register(Mage, MageAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ColorStyle, ColorStyleAdmin)


