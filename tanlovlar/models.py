from django.db import models


class Tanlovlar(models.Model):
    kalit = models.CharField(max_length=255)
    qiymat = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Tanlov"
        verbose_name_plural = "Tanlovlar"

    def __str__(self):
        return self.kalit