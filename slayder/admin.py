from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.html import format_html

from slayder.models import Slayder


class SlayderAdmin(admin.ModelAdmin):
    list_display = ('admin_photo','title', 'create', 'update', 'image',  'text')
    search_fields = ('title', 'text')
    list_filter = ('create', 'update')
    date_hierarchy = 'create'
    ordering = ('-create',)
    readonly_fields = ('admin_photo',)

    # paginator = Paginator

    def image(self, obj):
        return format_html('<img src="{0}"width="100" height="100" />'.format(obj.image.url))


admin.site.register(Slayder, SlayderAdmin)
