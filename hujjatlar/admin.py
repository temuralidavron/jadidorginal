from django.contrib import admin
from django.core.paginator import Paginator

from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, \
    Dissertatsiya


class AsarlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'file', 'create', 'update')
    list_display_links = ('title',  'jadid', 'file')
    search_fields = ('title',  'jadid',)
    list_per_page = 25
    list_filter = ('title', 'jadid',)

    # paginator = Paginator


class MaqolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'file', 'create', 'update')
    list_display_links = ('title',  'jadid', 'file')
    search_fields = ('title',  'jadid',)
    list_per_page = 25
    list_filter = ('title', 'jadid',)

    # paginator = Paginator


class TadqiqotlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'file', 'create', 'update')
    list_display_links = ('title',  'jadid', 'file')
    search_fields = ('title',  'jadid',)
    list_per_page = 25
    list_filter = ('title', 'jadid',)

    # paginator = Paginator


class SherlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'file', 'create', 'update')
    list_display_links = ('title',  'jadid', 'file')
    search_fields = ('title',  'jadid',)
    list_per_page = 25
    list_filter = ('title', 'jadid',)

    # paginator = Paginator


class HotiralarAdmin(admin.ModelAdmin):
    list_display = ('title', 'jadid', 'file', 'create', 'update')
    search_fields = ('title',  'jadid',)
    list_per_page = 25
    list_filter = ('title', 'jadid',)

    # paginator = Paginator


class HikmatlarAdmin(admin.ModelAdmin):
    list_display = ('text', 'create', 'update')
    # list_filter = ('text', 'create', 'update')
    search_fields = ('text',)
    list_per_page = 25


class Arxiv_hujjatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'file',)
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title',)

    # paginator = Paginator


class DissertatsiyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'create', 'update')
    list_display_links = ('title', 'file')
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title', 'file')

    # paginator = Paginator


admin.site.register(Asarlar, AsarlarAdmin)
admin.site.register(Maqolalar,  MaqolalarAdmin)
admin.site.register(Tadqiqotlar,  TadqiqotlarAdmin)
admin.site.register(Sherlar,  SherlarAdmin)
admin.site.register(Hotiralar,   HotiralarAdmin)
admin.site.register(Hikmatlar,  HikmatlarAdmin)
admin.site.register(Arxiv_hujjatlar,  Arxiv_hujjatlarAdmin)
admin.site.register(Dissertatsiya,   DissertatsiyaAdmin)


