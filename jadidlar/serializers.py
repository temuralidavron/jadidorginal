from rest_framework import serializers

from hujjatlar.serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, SherlarSerializer, \
    HotiralarSerializer
from jadidlar.models import Jadid
from hikmatli_sozlar.serializers import Hikmatli_sozlarSerializer


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = ('id', 'fullname', 'image', 'bio', 'birthday', 'die_day', 'order', 'create', 'update',
                  'hikmatli_sozlar', 'asarlar', 'maqolalar', 'tadqiqotlar', 'sherlar', 'hotiralar',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.jadid_images.all()
        hikmatli_sozlarlar = instance.hikmatli_sozlar.all()
        asarlar = instance.asarlar.all()
        maqolalar = instance.maqolalar.all()
        tadqiqotlar = instance.tadqiqotlar.all()
        sherlar = instance.sherlar.all()
        hotiralar = instance.hotiralar.all()
        if hikmatli_sozlarlar:
            data['hikmatli_sozlar'] = Hikmatli_sozlarSerializer(hikmatli_sozlarlar, many=True).data

        if asarlar:
            data['asarlar'] = AsarlarSerializer(asarlar, many=True).data

        if maqolalar:
            data['maqolalar'] = MaqolalarSerializer(maqolalar, many=True).data

        if tadqiqotlar:
            data['tadqiqotlar'] = TadqiqotlarSerializer(tadqiqotlar, many=True).data

        if sherlar:
            data['sherlar'] = SherlarSerializer(sherlar, many=True).data

        if hotiralar:
            data['hotiralar'] = HotiralarSerializer(hotiralar, many=True).data

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        if 'asarlar' in data:
            for asar in data['asarlar']:
                if 'file' in asar and asar['file']:
                    asar['file'] = request.build_absolute_uri(asar['file'])

        if 'maqolalar' in data:
            for maqola in data['maqolalar']:
                if 'file' in maqola and maqola['file']:
                    maqola['file'] = request.build_absolute_uri(maqola['file'])

        if 'hikmatli_sozlar' in data:
            for hikmatli_soz in data['hikmatli_sozlar']:
                if 'file' in hikmatli_soz and hikmatli_soz['file']:
                    hikmatli_soz['file'] = request.build_absolute_uri(hikmatli_soz['file'])

        if 'tadqiqotlar' in data:
            for tadqiqot in data['tadqiqotlar']:
                if 'file' in tadqiqot and tadqiqot['file']:
                    tadqiqot['file'] = request.build_absolute_uri(tadqiqot['file'])

        if 'sherlar' in data:
            for sher in data['sherlar']:
                if 'file' in sher and sher['file']:
                    sher['file'] = request.build_absolute_uri(sher['file'])

        if 'hotiralar' in data:
            for hotira in data['hotiralar']:
                if 'file' in hotira and hotira['file']:
                    hotira['file'] = request.build_absolute_uri(hotira['file'])

        return data