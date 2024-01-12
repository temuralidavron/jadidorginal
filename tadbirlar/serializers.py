from rest_framework import serializers
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar


class KanferensiyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanferensiyalar
        fields = '__all__'



class SeminarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminarlar
        fields = '__all__'


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'




