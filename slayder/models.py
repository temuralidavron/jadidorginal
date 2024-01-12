from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Slayder(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    text = RichTextField(verbose_name='Tavsiv')
    citations = models.CharField(max_length=255, verbose_name='Havolalar')
    image = models.ImageField(upload_to='slayder')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    citations = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayderlar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title
