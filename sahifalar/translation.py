from modeltranslation.translator import TranslationOptions, register

from sahifalar.models import Sahifalar


@register(Sahifalar)
class SahifalarTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
