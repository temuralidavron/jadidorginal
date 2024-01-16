from modeltranslation.translator import TranslationOptions, register

from manbalar.models import Audiolar, Videolar, Rasmlar


@register(Audiolar)
class AudiolarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Videolar)
class VideolarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Rasmlar)
class RasmlarTranslationOptions(TranslationOptions):
    fields = ('title',)