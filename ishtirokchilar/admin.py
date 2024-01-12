from django.contrib import admin
from django.utils.html import format_html

from ishtirokchilar.models import Ishtirokchilar


class IshtirokchilarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'image', 'fullname', 'position')
    list_display_links = ('fullname', 'position', 'image')
    search_fields = ('fullname', 'position')
    list_per_page = 25
    list_filter = ('fullname', 'position')
    readonly_fields = ('admin_photo',)


    # paginator = Paginator

    def image(self, obj):
        return format_html('<img src="{0}"width="" height="100" />'.format(obj.image.url))

admin.site.register(Ishtirokchilar,  IshtirokchilarAdmin)
