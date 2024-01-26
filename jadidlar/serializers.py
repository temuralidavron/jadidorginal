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
                        asar['file'] = f"https://jadidlar.pythonanywhere.com{asar['file']}"
                    if 'image' in asar and asar['image']:
                        asar['image'] = f"https://jadidlar.pythonanywhere.com{asar['image']}"

        if maqolalar:
            data['maqolalar'] = MaqolalarSerializer(maqolalar, many=True).data
            if 'maqolalar' in data:
                for maqola in data['maqolalar']:
                    if 'file' in maqola and maqola['file']:
                        maqola['file'] = f"https://jadidlar.pythonanywhere.com{maqola['file']}"
                    if 'image' in maqola and maqola['image']:
                        maqola['image'] = f"https://jadidlar.pythonanywhere.com{maqola['image']}"

        if tadqiqotlar:
            data['tadqiqotlar'] = TadqiqotlarSerializer(tadqiqotlar, many=True).data
            if 'tadqiqotlar' in data:
                for tadqiqot in data['tadqiqotlar']:
                    if 'file' in tadqiqot and tadqiqot['file']:
                        tadqiqot['file'] = f"https://jadidlar.pythonanywhere.com{tadqiqot['file']}"
                    if 'image' in tadqiqot and tadqiqot['image']:
                        tadqiqot['image'] = f"https://jadidlar.pythonanywhere.com{tadqiqot['image']}"
                    # Add more fields as needed

        if sherlar:
            data['sherlar'] = SherlarSerializer(sherlar, many=True).data
            if 'sherlar' in data:
                for sher in data['sherlar']:
                    if 'file' in sher and sher['file']:
                        sher['file'] = f"https://jadidlar.pythonanywhere.com{sher['file']}"
                    if 'image' in sher and sher['image']:
                        sher['image'] = f"https://jadidlar.pythonanywhere.com{sher['image']}"

        if hotiralar:
            data['hotiralar'] = HotiralarSerializer(hotiralar, many=True).data
            if 'hotiralar' in data:
                for hotira in data['hotiralar']:
                    if 'file' in hotira and hotira['file']:
                        hotira['file'] = f"https://jadidlar.pythonanywhere.com{hotira['file']}"
                    if 'image' in hotira and hotira['image']:
                        hotira['image'] = f"https://jadidlar.pythonanywhere.com{hotira['image']}"

        if images:
            data['images'] = [{'image': f"https://jadidlar.pythonanywhere.com{img.image.url}"} for img in images]

        return data
