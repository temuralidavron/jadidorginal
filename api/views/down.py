from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hujjatlar.models import Maqolalar, Asarlar, Tadqiqotlar, Sherlar, Hotiralar, Hikmatlar, Arxiv_hujjatlar, \
    Dissertatsiya
from matbuotlar.models import Matbuotlar
from sahifalar.models import Sahifalar


class FileDownAsarView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Asarlar.objects.get(id=pk)
        except Asarlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownMaqolaView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Maqolalar.objects.get(id=pk)
        except Maqolalar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownTadqiqotView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Tadqiqotlar.objects.get(id=pk)
        except Tadqiqotlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownSherView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Sherlar.objects.get(id=pk)
        except Sherlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownHotiraView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Hotiralar.objects.get(id=pk)
        except Hotiralar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownArxiv_hujjatView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Arxiv_hujjatlar.objects.get(id=pk)
        except Arxiv_hujjatlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownDissertatsiyaView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Dissertatsiya.objects.get(id=pk)
        except Dissertatsiya.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownMatbuotView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Matbuotlar.objects.get(id=pk)
        except Matbuotlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response


class FileDownSahifaView(APIView):
    def get(self, request, pk):
        try:
            file_instance = Sahifalar.objects.get(id=pk)
        except Sahifalar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = file_instance.file.path
        file_instance.count += 1
        file_instance.save()
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachmand; filename="{file_instance.title}"'
        return response