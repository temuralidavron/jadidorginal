from django.contrib import admin
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya, AsarlarFile, MaqolalarFile, TadqiqotlarFile, SherlarFile, HotiralarFile, Arxiv_hujjatlarFile, \
    DissertatsiyaFile


class AsarlarFileInline(admin.TabularInline):
    model = AsarlarFile


@admin.register(Asarlar)
class AsarlarAdmin(admin.ModelAdmin):
    inlines = [AsarlarFileInline]
    fields = ('title_uz', 'title_ru', 'jadid', 'image', 'file', 'turkiston_muxtoriyati', 'tadqiqotlar', 'til_va_imlo',
              'count')
    readonly_fields = ('count',)


class MaqolalarFileInline(admin.TabularInline):
    model = MaqolalarFile


@admin.register(Maqolalar)
class MaqolalarAdmin(admin.ModelAdmin):
    inlines = [MaqolalarFileInline]
    fields = ('title_uz', 'title_ru', 'jadid', 'image', 'file', 'turkiston_muxtoriyati', 'tadqiqotlar', 'til_va_imlo',
              'count',)
    readonly_fields = ('count',)


class TadqiqotlarFileInline(admin.TabularInline):
    model = TadqiqotlarFile


@admin.register(Tadqiqotlar)
class TadqiqotlarAdmin(admin.ModelAdmin):
    inlines = [TadqiqotlarFileInline]
    fields = ('title_uz', 'title_ru', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class SherlarFileInline(admin.TabularInline):
    model = SherlarFile


@admin.register(Sherlar)
class SherlarAdmin(admin.ModelAdmin):
    inlines = [SherlarFileInline]
    fields = ('title_uz', 'title_ru', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class HotiralarFileInline(admin.TabularInline):
    model = HotiralarFile


@admin.register(Hotiralar)
class HotiralarAdmin(admin.ModelAdmin):
    inlines = [HotiralarFileInline]
    fields = ('title_uz', 'title_ru', 'jadid', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class Arxiv_hujjatlarFileInline(admin.TabularInline):
    model = Arxiv_hujjatlarFile


@admin.register(Arxiv_hujjatlar)
class Arxiv_hujjatlarAdmin(admin.ModelAdmin):
    inlines = [Arxiv_hujjatlarFileInline]
    fields = ('title_uz', 'title_ru', 'image', 'file', 'type', 'count',)
    readonly_fields = ('count',)


class DissertatsiyaFileInline(admin.TabularInline):
    model = DissertatsiyaFile


@admin.register(Dissertatsiya)
class DissertatsiyaAdmin(admin.ModelAdmin):
    inlines = [DissertatsiyaFileInline]
    fields = ('title_uz', 'title_ru', 'image', 'file', 'count',)
    readonly_fields = ('count',)
