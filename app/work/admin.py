from django.contrib import admin
from work.models import Project, Visitor

class ProjectAdmin(admin.ModelAdmin):
    pass

class VisitorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Visitor, VisitorAdmin)

