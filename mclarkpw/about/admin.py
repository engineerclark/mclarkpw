from django.contrib import admin
from .models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'hide')
    
    def queryset(self, request):
        return self.model.including_hidden.get_queryset()
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('program', 'school', 'hide')
    
    def queryset(self, request):
        return self.model.including_hidden.get_queryset()

admin.site.register(Tag, TagAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(School, SchoolAdmin)