from django.contrib import admin
# from django.core.paginator import Paginator

from matbuotlar.models import Matbuot_categoriya, Matbuotlar


@admin.register(Matbuot_categoriya)
class Matbuot_categoriyaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title_uz', 'title_ru',)
    search_fields = ('title',)
    list_filter = ('title',)
    # paginator = Paginator


@admin.register(Matbuotlar)
class MatbuotlarAdmin(admin.ModelAdmin):
    list_display = ('categoriya',)
    fields = ('categoriya', 'title_uz', 'title_ru', 'image', 'file', 'count',)
    readonly_fields = ('count',)
    search_fields = ('title',)
    list_filter = ('title',)
    # paginator = Paginator
