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
            if 'asarlar' in data:
                for asar in data['asarlar']:
                    if 'file' in asar and asar['file']:
                        asar['file'] = f"http://127.0.0.1:8000{asar['file']}"
                    if 'image' in asar and asar['image']:
                        asar['image'] = f"http://127.0.0.1:8000{asar['image']}"

        if maqolalar:
            data['maqolalar'] = MaqolalarSerializer(maqolalar, many=True).data
            if 'maqolalar' in data:
                for maqola in data['maqolalar']:
                    if 'file' in maqola and maqola['file']:
                        maqola['file'] = f"http://127.0.0.1:8000{maqola['file']}"
                    if 'image' in maqola and maqola['image']:
                        maqola['image'] = f"http://127.0.0.1:8000{maqola['image']}"

        if tadqiqotlar:
            data['tadqiqotlar'] = MaqolalarSerializer(tadqiqotlar, many=True).data
            if 'tadqiqotlar' in data:
                for tadqiqot in data['tadqiqotlar']:
                    if 'file' in tadqiqot and tadqiqot['file']:
                        tadqiqot['file'] = f"http://127.0.0.1:8000{tadqiqot['file']}"
                    if 'image' in tadqiqot and tadqiqot['image']:
                        tadqiqot['image'] = f"http://127.0.0.1:8000{tadqiqot['image']}"
                    # Add more fields as needed

        if sherlar:
            data['sherlar'] = MaqolalarSerializer(sherlar, many=True).data
            if 'sherlar' in data:
                for sher in data['sherlar']:
                    if 'file' in sher and sher['file']:
                        sher['file'] = f"http://127.0.0.1:8000{sher['file']}"
                    if 'image' in sher and sher['image']:
                        sher['image'] = f"http://127.0.0.1:8000{sher['image']}"

        if hotiralar:
            data['hotiralar'] = MaqolalarSerializer(hotiralar, many=True).data
            if 'hotiralar' in data:
                for hotira in data['hotiralar']:
                    if 'file' in hotira and hotira['file']:
                        hotira['file'] = f"http://127.0.0.1:8000{hotira['file']}"
                    if 'image' in hotira and hotira['image']:
                        hotira['image'] = f"http://127.0.0.1:8000{hotira['image']}"

        if images:
            data['images'] = [{'image': f"http://127.0.0.1:8000{img.image.url}"} for img in images]

        return data
