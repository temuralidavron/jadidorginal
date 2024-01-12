from django.contrib import admin
# from django.core.paginator import Paginator

from hikmatli_sozlar.models import Hikmatli_sozlar

class Hikmatli_sozlarAdmin(admin.ModelAdmin):
    list_display = ('jadid', 'text')
    list_display_links = ('jadid', 'text')
    search_fields = ('jadid__fullname', 'text')
    list_filter = ('jadid', 'text')
    # paginator = Paginator

admin.site.register(Hikmatli_sozlar, Hikmatli_sozlarAdmin)
