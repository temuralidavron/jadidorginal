from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Kanferensiyalar(models.Model):
    title = models.CharField(max_length=20, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'Kanferensiya'
        verbose_name_plural = 'Kanferensiyalar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title


class Seminarlar(models.Model):
    title = models.CharField(max_length=20, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminarlar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title


class Yangiliklar(models.Model):
    title = models.CharField(max_length=20, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title