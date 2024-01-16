from modeltranslation.translator import TranslationOptions, register

from foydali_havolalar.models import Foydali_havolalar


@register(Foydali_havolalar)
class Foydali_havolalarTranslationOptions(TranslationOptions):
    fields = ('title',)
