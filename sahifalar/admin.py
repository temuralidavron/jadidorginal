from django.contrib import admin

from sahifalar.models import Sahifalar


class SahifalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'update')
    list_filter = ("title",)
    search_fields = ['title',]


admin.site.register(Sahifalar,  SahifalarAdmin)