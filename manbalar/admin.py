from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.html import format_html

from manbalar.models import Rasmlar, Audiolar, Videolar


class RasimlarAdmin(admin.ModelAdmin):
    list_display = ['admin_photo', 'title', 'image', 'file', 'create', 'update']
    list_display_links = ['title', 'image', 'file', 'create', 'update']
    search_fields = ['title',]
    list_per_page = 25
    list_filter = ['title', 'file']
    readonly_fields = ('admin_photo',)
    save_as = False
    save_as_continue = True
    save_on_top = False
    # paginator = Paginator

class AudiolarAdmin(admin.ModelAdmin):
    list_display = ['title', 'audio', 'file', 'create', 'update']
    list_display_links = ['title', 'audio', 'file', 'create', 'update']
    search_fields = ['title',]
    list_per_page = 25
    list_filter = ['title', 'file']
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # paginator = Paginator


class VideolarAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'file', 'create', 'update']
    list_display_links = ['title', 'video', 'file', 'create', 'update']
    search_fields = ['title',]
    list_per_page = 25
    list_filter = ['title', 'file']
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # paginator = Paginator


    def image(self, obj):
        return format_html('<img src="{0}"width="100" height="100" />'.format(obj.image.url))



admin.site.register(Rasmlar,  RasimlarAdmin)
admin.site.register(Audiolar,  AudiolarAdmin)
admin.site.register(Videolar,   VideolarAdmin)
