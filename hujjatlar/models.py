from ckeditor.fields import RichTextField
from django.db import models

from jadidlar.models import Jadid


class Asarlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asar'
        verbose_name_plural = 'Asarlar'


class AsarlarFile(models.Model):
    asarlar = models.ForeignKey(Asarlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/asarlar')

    def __str__(self):
        return self.file.url


class Maqolalar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/maqolalar', verbose_name='fayl')
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class MaqolalarFile(models.Model):
    maqolalar = models.ForeignKey(Maqolalar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/maqolalar')

    def __str__(self):
        return self.file.url


class Tadqiqotlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/tadqiqotlar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tadqiqot'
        verbose_name_plural = 'Tadqiqotlar'


class TadqiqotlarFile(models.Model):
    tadqiqotlar = models.ForeignKey(Tadqiqotlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/tadqiqotlar')

    def __str__(self):
        return self.file.url


class Sherlar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/sherlar')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sher'
        verbose_name_plural = 'Sherlar'


class SherlarFile(models.Model):
    sherlar = models.ForeignKey(Sherlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/sherlar')

    def __str__(self):
        return self.file.url


class Hotiralar(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/hotiralar', verbose_name='fayl')
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')

    class Meta:
        verbose_name = 'Hotira'
        verbose_name_plural = 'Hotiralar'


class HotiralarFile(models.Model):
    hotiralar = models.ForeignKey(Hotiralar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/hotiralar')

    def __str__(self):
        return self.file.url


class Hikmatlar(models.Model):
    text = RichTextField(verbose_name='hikmatli soz')
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')

    class Meta:
        verbose_name = 'Hikmat'
        verbose_name_plural = 'Hikmatlar'

    def __str__(self):
        return self.text


class Arxiv_hujjatlar(models.Model):
    ARXIV = 'ARXIV'
    SKANER = 'SKANER'
    TYPE_CHOICE = (
        (ARXIV, 'ARXIV'),
        (SKANER, 'SKANER'),
    )

    title = models.CharField(max_length=255, verbose_name='nomi')
    type = models.CharField(max_length=6, choices=TYPE_CHOICE, verbose_name='turi', default=ARXIV)
    # arxiv = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/arxiv_hujjatlar', verbose_name='fayl')

    class Meta:
        verbose_name = 'Arxiv hujjat'
        verbose_name_plural = 'Arxiv hujjatlar'


class Arxiv_hujjatlarFile(models.Model):
    arxiv_hujjatlar = models.ForeignKey(Arxiv_hujjatlar, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/arxiv_hujjatlar')

    def __str__(self):
        return self.file.url


class Dissertatsiya(models.Model):
    title = models.CharField(max_length=255, verbose_name='nomi')
    file = models.FileField(upload_to='files/dissertatsiya', verbose_name='fayl')
    create = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana')
    update = models.DateTimeField(auto_now=True, verbose_name='o`zgartirilgan sana')

    class Meta:
        verbose_name = 'Dissertatsiya'
        verbose_name_plural = 'Dissertatsiyalar'


class DissertatsiyaFile(models.Model):
    dissertatsiya = models.ForeignKey(Dissertatsiya, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='files/dissertatsiya')

    def __str__(self):
        return self.file.url
