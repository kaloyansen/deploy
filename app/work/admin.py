from django.contrib import admin
from django.db import models
from work.models import Project, Visitor, Page, ColorStyle

class PageAdmin(admin.ModelAdmin): pass
class PageInline(admin.TabularInline): model = Page
class VisitorAdmin(admin.ModelAdmin): inlines = [ PageInline ]
class ProjectAdmin(admin.ModelAdmin): pass
class ColorStyleAdmin(admin.ModelAdmin): pass

admin.site.register(Page, PageAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ColorStyle, ColorStyleAdmin)


