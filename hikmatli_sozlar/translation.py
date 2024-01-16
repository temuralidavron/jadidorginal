from modeltranslation.translator import TranslationOptions, register

from hikmatli_sozlar.models import Hikmatli_sozlar


@register(Hikmatli_sozlar)
class Hikmatli_sozlarTranslationOptions(TranslationOptions):
    fields = ('text',)
