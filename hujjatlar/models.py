from ckeditor.fields import RichTextField
from django.db import models

from jadidlar.models import Jadid


class Asarlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/asarlar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asar'
        verbose_name_plural = 'Asarlar'

    def __str__(self):
        return self.title


class Maqolalar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/maqolalar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.title


class Tadqiqotlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/tadqiqotlar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqotlar'

    def __str__(self):
        return self.title


class Sherlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/sherlar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sher'
        verbose_name_plural = 'Sherlar'

    def __str__(self):
        return self.title


class Hotiralar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/hotiralar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hotira'
        verbose_name_plural = 'Hotiralar'

    def __str__(self):
        return self.title


class Hikmatlar(models.Model):
    text = RichTextField(verbose_name='hikmatli soz')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hikmat'
        verbose_name_plural = 'Hikmatlar'

    def __str__(self):
        return self.text


class Arxiv_hujjatlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    MY_CHOICES = [
        ('value1', 'Royxat'),
        ('value2', 'Skanner'),
    ]
    # arxiv = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/arxiv_hujjatlar')

    class Meta:
        verbose_name = 'Arxiv_hujjat'
        verbose_name_plural = 'Arxiv_hujjatlar'

    def __str__(self):
        return self.title


class Dissertatsiya(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    file = models.FileField(upload_to='files/dissertatsiya')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dissertatsiya'
        verbose_name_plural = 'Dissertatsiyalar'

    def __str__(self):
        return self.title