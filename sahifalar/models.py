from ckeditor.fields import RichTextField
from django.db import models


class Sahifalar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Sahifa nomi')
    text = RichTextField(verbose_name='Matn')
    file = models.FileField(upload_to='files/', verbose_name='Fayl')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    update = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    class  Meta:
        verbose_name = 'Sahifa'
        verbose_name_plural = 'Sahifalar'

    def __str__(self):
        return self.title

