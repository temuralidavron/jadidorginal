from django.contrib import admin
# from django.core.paginator import Paginator

from hikmatli_sozlar.models import Hikmatli_sozlar


@admin.register(Hikmatli_sozlar)
class Hikmatli_sozlarAdmin(admin.ModelAdmin):
    list_display = ('jadid', )
    fields = ('jadid', 'text_uz', 'text_ru',)
    list_display_links = ('jadid',)
    search_fields = ('jadid__fullname', 'text')
    list_filter = ('jadid', 'text')
    # paginator = Paginator



