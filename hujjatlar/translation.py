from modeltranslation.translator import TranslationOptions, register

from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya


@register(Asarlar)
class AsarlarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Maqolalar)
class MaqolalarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tadqiqotlar)
class TadqiqotlarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Sherlar)
class SherlarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Hotiralar)
class HotiralarTranslationOptions(TranslationOptions):
    fields = ('title',)


# @register(Hikmatlar)
# class HikmatlarTranslationOptions(TranslationOptions):
#     fields = ('text',)


@register(Arxiv_hujjatlar)
class Arxiv_hujjatlarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Dissertatsiya)
class DissertatsiyaTranslationOptions(TranslationOptions):
    fields = ('title',)