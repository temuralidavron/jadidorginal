from django.db import models


class Matbuot_categoriya(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Matbuot Categoriya'
        verbose_name_plural = 'Matbuot Categoriyalar'


class Matbuotlar(models.Model):
    categoriya = models.ForeignKey(Matbuot_categoriya, on_delete=models.CASCADE,related_name='categoriy')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='matbuotlar')
    file = models.FileField(upload_to='matbuotlar')
    # count = models.BigIntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Matbuot'
        verbose_name_plural = 'Matbuotlar'
