from django.contrib import admin

from sahifalar.models import Sahifalar, SahifalarFile


class SahifalarFileInline(admin.TabularInline):
    model = SahifalarFile


@admin.register(Sahifalar)
class SahifalarAdmin(admin.ModelAdmin):
    inlines = [SahifalarFileInline]
    fields = ('title_uz', 'title_ru', 'text_uz', 'text_ru', 'image', 'file', 'count',)
    readonly_fields = ('count',)