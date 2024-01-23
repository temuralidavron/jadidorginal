from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from hikmatli_sozlar.models import Hikmatli_sozlar
from hikmatli_sozlar.serializers import Hikmatli_sozlarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class Hikmatli_sozlarListView(ListAPIView):
    search_fields = ['text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Hikmatli_sozlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Hikmatli_sozlar.objects.all()


@api_view(['GET'])
def hikmatli_sozlardetail(request, pk):
    hikmatli_sozlar = get_object_or_404(Hikmatli_sozlar, pk=pk)
    serializer = Hikmatli_sozlarSerializer(hikmatli_sozlar, context={'request': request})
    return Response(serializer.data)
