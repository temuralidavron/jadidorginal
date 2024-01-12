from rest_framework import generics
from hikmatli_sozlar.models import Hikmatli_sozlar
from hikmatli_sozlar.serializers import Hikmatli_sozlarSerializer


class Hikmatli_sozlarListCreateView(generics.ListAPIView):
    queryset = Hikmatli_sozlar.objects.all()
    serializer_class = Hikmatli_sozlarSerializer

# class Hikmatli_sozlarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hikmatli_sozlar.objects.all()
#     serializer_class = Hikmatli_sozlarSerializer
