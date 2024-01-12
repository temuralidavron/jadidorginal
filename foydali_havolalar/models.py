from django.db import models
from django.utils.safestring import mark_safe

from ckeditor.fields import RichTextField


class Foydali_havolalar(models.Model):
    title = models.CharField(max_length=20, verbose_name='nomi')
    link = RichTextField(verbose_name='link')
    logo_image = models.ImageField()

    class Meta:
        verbose_name = 'Foydali_havola'
        verbose_name_plural = 'Foydali_havolalar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.logo_image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title
