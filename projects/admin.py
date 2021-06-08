from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'modified',)


admin.site.register(Project, ProjectAdmin)
