from django.db import models


class Matbuotlar(models.Model):
    Tarix = 'Tarix'
    Siyosat = 'Siyosat'
    Iqtisod = 'Iqtisod'
    Madaniyat_va_sanat = 'Madaniyat va sanat'
    Ijtimoiy_masalalar_va_din = 'Ijtimoiy masalalar va din'
    Adabiyot = 'Adabiyot'
    Talim_Tarbiya = 'Talim - Tarbiya'
    Boshqa_masalalar = 'Boshqa masalalar'
    Bibliografik_korsatkich = 'Bibliografik korsatkich'

    TYPE_CHOICE = (
        (Tarix, 'Tarix'),
        (Siyosat, 'Siyosat'),
        (Iqtisod, 'Iqtisod'),
        (Madaniyat_va_sanat, 'Madaniyat va sanat'),
        (Ijtimoiy_masalalar_va_din, 'Ijtimoiy masalalar va din'),
        (Adabiyot, 'Adabiyot'),
        (Talim_Tarbiya, 'Talim - Tarbiya'),
        (Boshqa_masalalar, 'Boshqa masalalar'),
        (Bibliografik_korsatkich, 'Bibliografik korsatkich'),
    )
    type = models.CharField(max_length=30, choices=TYPE_CHOICE, verbose_name='turi', default=Tarix)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='matbuotlar')
    file = models.FileField(upload_to='matbuotlar')
    count = models.BigIntegerField(null=True, blank=True, default=0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Matbuot'
        verbose_name_plural = 'Matbuotlar'
