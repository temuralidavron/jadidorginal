from django.contrib import admin
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, \
    Dissertatsiya, AsarlarFile, MaqolalarFile, TadqiqotlarFile, SherlarFile, HotiralarFile, Arxiv_hujjatlarFile, \
    DissertatsiyaFile


class AsarlarFileInline(admin.TabularInline):
    model = AsarlarFile


@admin.register(Asarlar)
class AsarlarAdmin(admin.ModelAdmin):
    inlines = [AsarlarFileInline]


class MaqolalarFileInline(admin.TabularInline):
    model = MaqolalarFile


@admin.register(Maqolalar)
class MaqolalarAdmin(admin.ModelAdmin):
    inlines = [MaqolalarFileInline]


class TadqiqotlarFileInline(admin.TabularInline):
    model = TadqiqotlarFile


@admin.register(Tadqiqotlar)
class TadqiqotlarAdmin(admin.ModelAdmin):
    inlines = [TadqiqotlarFileInline]


class SherlarFileInline(admin.TabularInline):
    model = SherlarFile


@admin.register(Sherlar)
class SherlarAdmin(admin.ModelAdmin):
    inlines = [SherlarFileInline]


class HotiralarFileInline(admin.TabularInline):
    model = HotiralarFile


@admin.register(Hotiralar)
class HotiralarAdmin(admin.ModelAdmin):
    inlines = [HotiralarFileInline]


class HikmatlarAdmin(admin.ModelAdmin):
    list_display = ('text', 'create', 'update')
    # list_filter = ('text', 'create', 'update')
    search_fields = ('text',)
    list_per_page = 25


class Arxiv_hujjatlarFileInline(admin.TabularInline):
    model = Arxiv_hujjatlarFile


@admin.register(Arxiv_hujjatlar)
class Arxiv_hujjatlarAdmin(admin.ModelAdmin):
    inlines = [Arxiv_hujjatlarFileInline]


class DissertatsiyaFileInline(admin.TabularInline):
    model = DissertatsiyaFile


@admin.register(Dissertatsiya)
class DissertatsiyaAdmin(admin.ModelAdmin):
    inlines = [DissertatsiyaFileInline]
