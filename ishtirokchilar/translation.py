from modeltranslation.translator import TranslationOptions, register

from ishtirokchilar.models import Ishtirokchilar


@register(Ishtirokchilar)
class IshtirokchilarTranslationOptions(TranslationOptions):
    fields = ('fullname', 'position')
