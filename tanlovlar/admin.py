from django.contrib import admin

from tanlovlar.models import Tanlovlar


class TanlovlarAdmin(admin.ModelAdmin):
    list_display = ('type', 'qiymat',)
    list_display_links = ('type', 'qiymat',)
    list_per_page = 25

admin.site.register(Tanlovlar,  TanlovlarAdmin)