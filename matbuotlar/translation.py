from modeltranslation.translator import TranslationOptions,register

from matbuotlar.models import Matbuotlar


@register(Matbuotlar)
class MatbuotTranslationOptions(TranslationOptions):
    fields = ('title',)
