from rest_framework import serializers
from sahifalar.models import Sahifalar


class SahifalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sahifalar
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            data['files'] = [{'file': img.file.url} for img in files]

        return data
