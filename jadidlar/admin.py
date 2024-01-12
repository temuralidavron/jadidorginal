from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

from jadidlar.models import Jadid


@admin.register(Jadid)
class JadidAdmin(admin.ModelAdmin):
    list_display = ("fullname_uz", 'admin_photo', 'birthday', 'die_day', 'create', 'update', 'order')
    search_fields = ('fullname_uz', 'birthday')
    list_filter = ('create', 'update', 'order')
    date_hierarchy = 'create'
    ordering = ('-create',)

    readonly_fields = ('admin_photo',)

    def image(self, obj):
        return format_html('<img src="{0}"width="" height="100" />'.format(obj.image.url))

# class JadidAdminTRanslation(JadidAdmin, TranslationAdmin):
#     list_display = ("fullname",)
