from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe


class Kanferensiyalar(models.Model):
    title = models.CharField(max_length=200, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kanferensiya'
        verbose_name_plural = 'Kanferensiyalar'


class KanferensiyalarImage(models.Model):
    kanferensiya = models.ForeignKey(Kanferensiyalar, on_delete=models.CASCADE,
                                       related_name='kanferensiya_images')
    image = models.ImageField()

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True


class Seminarlar(models.Model):
    title = models.CharField(max_length=200, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminarlar'

class SeminarlarImage(models.Model):
    seminar = models.ForeignKey(Seminarlar, on_delete=models.CASCADE,
                                       related_name='seminar_images')
    image = models.ImageField()

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True




class Yangiliklar(models.Model):
    title = models.CharField(max_length=200, verbose_name='nomi')
    text = RichTextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

class YangiliklarImage(models.Model):
    yangilik = models.ForeignKey(Yangiliklar, on_delete=models.CASCADE,
                                       related_name='yangilik_images')
    image = models.ImageField()

    def __str__(self):
        return self.image.url

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True

