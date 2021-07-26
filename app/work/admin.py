from django.contrib import admin
from django.db import models
# from mdeditor.widgets import MDEditorWidget

from work.models import Project, Visitor, Page

class PageAdmin(admin.ModelAdmin): pass
class PageInline(admin.TabularInline): model = Page
class VisitorAdmin(admin.ModelAdmin): inlines = [ PageInline ]
class ProjectAdmin(admin.ModelAdmin): pass

admin.site.register(Page, PageAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Project, ProjectAdmin)


