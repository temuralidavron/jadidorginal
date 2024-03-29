from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from jadidlar.models import Jadid
from jadidlar.serializers import JadidSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class JadidlarListView(ListAPIView):
    search_fields = ['fullname', 'bio']
    filter_backends = (filters.SearchFilter,)
    serializer_class = JadidSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Jadid.objects.all().order_by('order')

@api_view(['GET'])
def jadidlardetail(request, pk):
    jadidlar = get_object_or_404(Jadid, pk=pk)
    serializer = JadidSerializer(jadidlar, context={'request': request})
    return Response(serializer.data)
