from django.contrib import admin
from django.utils.html import format_html

from manbalar.models import Rasmlar, Audiolar, Videolar, AudioFile, VideoFile, RasmlarImage


class RasmlarImageInline(admin.TabularInline):
    model = RasmlarImage
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


@admin.register(Rasmlar)
class RasimlarAdmin(admin.ModelAdmin):
    inlines = [RasmlarImageInline]
    list_display = ('title', 'display_admin_photo',)
    fields = ('title_uz', 'title_ru', 'image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 25
    list_max_show_all = 100
    save_as = False
    save_as_continue = True
    save_on_top = False
    readonly_fields = ('display_admin_photo', 'display_images',)

    def display_admin_photo(self, obj):
        return format_html('<img src="{0}" width="100" height="100"  />'.format(obj.image.url))

    display_admin_photo.short_description = 'Rasm'
    display_admin_photo.allow_tags = True

    def display_images(self, obj):
        images = obj.rasimlar.all()  # Adjust the related name accordingly
        return format_html(''.join(
            '<img src="{0}" width="100" height="100" style="margin-right: 10px;"  />'.format(img.image.url) for img in
            images))

    display_images.short_description = 'Images'
    display_images.allow_tags = True

    def image(self, obj):
        return format_html('<img src="{0}" width="100" height="100" />'.format(obj.image.url))

    image.short_description = 'Rasm'
    image.allow_tags = True


class AudioInline(admin.TabularInline):
    model = AudioFile
    extra = 1


@admin.register(Audiolar)
class AudiolarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_audio_player', 'display_file_link')
    fields = ('title_uz', 'title_ru', 'audio', 'file',)

    def display_audio_player(self, obj):
        return format_html('<audio controls><source src="{}" type="audio/mp3"></audio>', obj.audio.url)

    display_audio_player.short_description = 'Audio Player'

    def display_file_link(self, obj):
        return format_html('<a href="{}" download>{}</a>', obj.file.url, obj.file.name)

    display_file_link.short_description = 'File Download Link'

    inlines = [AudioInline]  # Add the inline to the admin model


class VideoInline(admin.TabularInline):
    model = VideoFile
    extra = 0


@admin.register(Videolar)
class VideolarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_video_player')
    fields = ('title_uz', 'title_ru', 'video', 'file',)

    def display_video_player(self, obj):
        return format_html('<video width="320" height="240" controls><source src="{}" type="video/mp4"></video>',
                           obj.video.url)

    display_video_player.short_description = 'Video Player'

    def display_file_link(self, obj):
        return format_html('<a href="{}" download>{}</a>', obj.file.url, obj.file.name)

    display_file_link.short_description = 'File Download Link'
    inlines = [VideoInline]  # Add the inline to the admin model


def image(self, obj):
    return format_html('<img src="{0}"width="100" height="100" />'.format(obj.image.url))
