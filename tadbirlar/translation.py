from modeltranslation.translator import TranslationOptions, register

from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar


@register(Kanferensiyalar)
class KanferensiyalarTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Seminarlar)
class SeminarlarTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
