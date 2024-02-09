from django.contrib import admin

from sahifalar.models import Sahifalar, SahifalarFile


class SahifalarFileInline(admin.TabularInline):
    model = SahifalarFile


@admin.register(Sahifalar)
class SahifalarAdmin(admin.ModelAdmin):
    inlines = [SahifalarFileInline]
    fields = ('title_uz', 'title_ru', 'title_en', 'text_uz', 'text_ru', 'text_en', 'image', 'file', 'count',)
    readonly_fields = ('count',)