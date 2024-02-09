from django.db import models
from django.utils.safestring import mark_safe

# from ckeditor.fields import RichTextField


class Foydali_havolalar(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi', blank=True, null=True)
    link = models.URLField(verbose_name='link')
    logo_image = models.ImageField(blank=True, null=True, upload_to='logo_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Foydali_havola'
        verbose_name_plural = 'Foydali_havolalar'


class Foydali_havolalarImage(models.Model):
    foydali_havola = models.ForeignKey(Foydali_havolalar, on_delete=models.CASCADE,
                                       related_name='foydali_havola_images')
    image = models.ImageField(blank=True, null=True, upload_to='foydali_havola_images/')

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.logo_image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True
