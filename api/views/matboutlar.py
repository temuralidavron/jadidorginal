from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from matbuotlar.models import Matbuot_categoriya, Matbuotlar
from matbuotlar.serializers import Matbuot_categoriyaSerializer, MatbuotlarSerializer

from rest_framework.decorators import api_view


class Matbuot_categoriyaListView(ListAPIView):
    serializer_class = Matbuot_categoriyaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Matbuot_categoriya.objects.all()


@api_view(['GET'])
def matbuot_categoriyadetail(request, pk):
    matbuotlar = get_object_or_404(Matbuot_categoriya, pk=pk)
    serializer = Matbuot_categoriyaSerializer(matbuotlar)
    return Response(serializer.data)


class MatbuotlarListView(ListAPIView):
    serializer_class = MatbuotlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Matbuotlar.objects.all()


@api_view(['GET'])
def matbuotlardetail(request, pk):
    matbuotlar = get_object_or_404(Matbuotlar, pk=pk)
    serializer = MatbuotlarSerializer(matbuotlar)
    return Response(serializer.data)
