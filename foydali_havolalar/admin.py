from django.contrib import admin
from django.utils.html import format_html

from foydali_havolalar.models import Foydali_havolalar


class Foydali_havolalarAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'title', 'link', 'logo_image',)
    list_display_links = ('title', 'link')
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('admin_photo',)
    # paginator = Paginator

    def logo_image(self, obj):
        return format_html('<img src="{0}"width="100" height="100" />'.format(obj.logo_image.url))



admin.site.register(Foydali_havolalar,  Foydali_havolalarAdmin)
