from django.contrib import admin
from django.utils.html import format_html
from slayder.models import Slayder, SlayderImage


class SlayderImageInline(admin.TabularInline):
    model = SlayderImage
    fields = ('image',)
    max_num = 10
    min_num = 1
    can_delete = False
    show_change_link = True
    show_add_button = True
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'
    list_display = ('image',)
    ordering = ('image',)
    extra = 0



@admin.register(Slayder)
class SlayderAdmin(admin.ModelAdmin):
    inlines = [SlayderImageInline]
    list_display = ('title', 'display_admin_photo',)
    fields = ('title_uz', 'title_ru', 'text_uz', 'text_ru', 'image', 'citations',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images', )

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.image.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.slayder_images.all()  # Adjust the related name accordingly
        return format_html(''.join('<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True

    def logo_image(self, obj):

        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.logo_image.url))




    logo_image.short_description = 'Rasm'
    logo_image.allow_tags = True
