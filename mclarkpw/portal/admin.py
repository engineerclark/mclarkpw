from django.contrib import admin
from .models import AuthToken

class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('value', 'user', 'expiration')

admin.site.register(AuthToken, AuthTokenAdmin)