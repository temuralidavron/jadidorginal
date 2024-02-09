from ckeditor.fields import RichTextField
from django.db import models

from jadidlar.models import Jadid


class Hikmatli_sozlar(models.Model):
    jadid = models.ForeignKey(Jadid, on_delete=models.CASCADE, related_name='hikmatli_sozlar')
    text = RichTextField(verbose_name='Hikmatli soz', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hikmatli soz'
        verbose_name_plural = 'Hikmatli sozlar'

    def __str__(self):
        return self.text
