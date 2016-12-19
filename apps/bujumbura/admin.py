from django.contrib import admin
from apps.bujumbura.models import apiKeys, ButtonTable

class ButtonAdmin(admin.ModelAdmin):
    list_display = ['button', 'sender', 'date_registered']
    ordering = ['date_registered']

admin.site.register(apiKeys)
admin.site.register(ButtonTable, ButtonAdmin)

# Register your models here.
