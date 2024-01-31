from django.contrib import admin
# from django.core.paginator import Paginator

from matbuotlar.models import Matbuotlar


@admin.register(Matbuotlar)
class MatbuotlarAdmin(admin.ModelAdmin):
    list_display = ('type', 'title',)
    fields = ('type', 'title_uz', 'title_ru', 'image', 'file', 'count',)
    readonly_fields = ('count',)
    search_fields = ('title',)
    list_filter = ('title',)
    # paginator = Paginator
