from rest_framework import generics
from foydali_havolalar.models import Foydali_havolalar
from foydali_havolalar.serializers import Foydali_havolalarSerializer


class Foydali_havolalarListCreateView(generics.ListAPIView):
    queryset = Foydali_havolalar.objects.all()
    serializer_class = Foydali_havolalarSerializer

# class Foydali_havolalarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Foydali_havolalar.objects.all()
#     serializer_class = Foydali_havolalarSerializer
