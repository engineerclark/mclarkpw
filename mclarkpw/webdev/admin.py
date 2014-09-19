from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
