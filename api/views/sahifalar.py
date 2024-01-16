from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from sahifalar.models import Sahifalar
from sahifalar.serializers import SahifalarSerializer

from rest_framework.decorators import api_view


class SahifalarListView(ListAPIView):
    serializer_class = SahifalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Sahifalar.objects.all()


@api_view(['GET'])
def sahifalardetail(request, pk):
    sahifalar = get_object_or_404(Sahifalar, pk=pk)
    serializer = SahifalarSerializer(sahifalar)
    return Response(serializer.data)
