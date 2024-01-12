from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Jadid(models.Model):
    fullname = models.CharField(max_length=255)
    birthday = models.DateField()
    die_day = models.DateField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/jadid')
    order = models.IntegerField(default=0)
    bio = RichTextField()

    class Meta:
        verbose_name = 'Jadid'
        verbose_name_plural = 'Jadidlar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.fullname
