from django.db import models


class Tanlovlar(models.Model):
    Telegram = 'Telegram'
    Instagram = 'Instagram'
    Facebook = 'Facebook'
    Email = 'Email'
    Telefon = 'Telefon'
    TYPE_CHOICE = (
        (Telegram, 'Telegram'),
        (Instagram, 'Instagram'),
        (Facebook, 'Facebook'),
        (Email, 'Email'),
        (Telefon, 'Telefon'),
    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICE, verbose_name='turi', default=Telegram)

    qiymat = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Tanlov"
        verbose_name_plural = "Tanlovlar"

    def __str__(self):
        return self.type