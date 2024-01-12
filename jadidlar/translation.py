from modeltranslation.translator import TranslationOptions, register

from jadidlar.models import Jadid


@register(Jadid)
class JadidTranslationOptions(TranslationOptions):
    fields = ('fullname', 'bio')
