from django.db import models
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


def validate_audio_extension(value):
    allowed_extensions = ['.mp3', '.wav', '.ogg']  # Qo'shimcha audio formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat MP3, WAV yoki OGG formatlari qo\'llaniladi.'))


class Audiolar(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi')
    audio = models.FileField(upload_to='audios/', validators=[validate_audio_extension])
    file = models.FileField(upload_to='files/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audiolar'

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        content_type = self.audio.file.content_type
        allowed_content_types = ['audio/mpeg', 'audio/wav', 'audio/ogg']  # Qo'shimcha audio formatlarni qo'shing
        if content_type not in allowed_content_types:
            raise ValidationError(_('Faqat MP3, WAV yoki OGG formatlari qo\'llaniladi.'))


def validate_video_extension(value):
    allowed_extensions = ['.mp4', '.avi', '.mkv']  # Qo'shimcha video formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat MP4, AVI yoki MKV formatlari qo\'llaniladi.'))


class Videolar(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi')
    video = models.FileField(upload_to='videos/', validators=[validate_video_extension])
    file = models.FileField(upload_to='files/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        content_type = self.video.file.content_type
        allowed_content_types = ['video/mp4', 'video/x-msvideo',
                                 'video/x-matroska']  # Qo'shimcha video formatlarni qo'shing
        if content_type not in allowed_content_types:
            raise ValidationError(_('Faqat MP4, AVI yoki MKV formatlari qo\'llaniladi.'))


def validate_image_extension(value):
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Qo'shimcha rasm formatlarni qo'shing
    if not any(value.name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Faqat JPEG, JPG, PNG yoki GIF formatlari qo\'llaniladi.'))


class Rasmlar(models.Model):
    title = models.CharField(max_length=100, verbose_name='nomi')
    image = models.ImageField(upload_to='images/', validators=[validate_image_extension])
    file = models.FileField(upload_to='files/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))

    admin_photo.short_description = 'Rasm'
    admin_photo.allow_tags = True


    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        content_type = self.image.file.content_type
        allowed_content_types = ['image/jpeg', 'image/jpg', 'image/png',
                                 'image/gif']  # Qo'shimcha rasm formatlarni qo'shing
        if content_type not in allowed_content_types:
            raise ValidationError(_('Faqat JPEG, JPG, PNG yoki GIF formatlari qo\'llaniladi.'))

    def save(self, *args, **kwargs):
        # 5 ta rasm qo'shishni tekshirish
        if not self.pk and Rasmlar.objects.count() >= 100:
            raise ValidationError(_('Faqat 100 ta rasm qo\'shishingiz mumkin.'))
        super().save(*args, **kwargs)



