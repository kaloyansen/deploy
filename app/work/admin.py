from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

from work.models import Project, Visitor


class ProjectAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {	'widget': MDEditorWidget }
	}


class VisitorAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Visitor, VisitorAdmin)

