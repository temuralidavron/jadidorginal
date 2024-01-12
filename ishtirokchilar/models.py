from django.db import models
from django.utils.safestring import mark_safe


class Ishtirokchilar(models.Model):
    fullname = models.CharField(max_length=20)
    position = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'Ishtirokchi'
        verbose_name_plural = 'Ishtirokchilar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.fullname
