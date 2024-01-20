from modeltranslation.translator import TranslationOptions,register

from matbuotlar.models import Matbuotlar, Matbuot_categoriya


@register(Matbuot_categoriya)
class Matbuot_categoriyaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Matbuotlar)
class MatbuotTranslationOptions(TranslationOptions):
    fields = ('title',)
