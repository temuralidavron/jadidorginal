from modeltranslation.translator import TranslationOptions, register

from slayder.models import Slayder


@register(Slayder)
class SlayderTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
