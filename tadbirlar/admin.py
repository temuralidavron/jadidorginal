from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.html import format_html

from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar


class KonferensiyalarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'title', 'text', 'image',)
    list_display_links = ('title', 'text', 'image',)
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title',)
    readonly_fields = ('admin_photo',)

    # paginator = Paginator


class SeminarlarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'title', 'text', 'image',)
    list_display_links = ('title', 'text', 'image',)
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title',)
    readonly_fields = ('admin_photo',)

    # paginator = Paginator


class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'title', 'text', 'image',)
    list_display_links = ('title', 'text', 'image',)
    search_fields = ('title',)
    list_per_page = 25
    list_filter = ('title',)
    readonly_fields = ('admin_photo',)

    # paginator = Paginator

    def image(self, obj):
        return format_html('<img src="{0}"width="100" height="100" />'.format(obj.image.url))



admin.site.register(Kanferensiyalar,  KonferensiyalarAdmin)
admin.site.register(Seminarlar,  SeminarlarAdmin)
admin.site.register(Yangiliklar,   YangiliklarAdmin)
