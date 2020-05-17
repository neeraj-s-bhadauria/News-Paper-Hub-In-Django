from django.contrib import admin
from .models import NewsSites


class HubAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ['name']
    list_filter = ("name",)


admin.site.register(NewsSites, HubAdmin)
