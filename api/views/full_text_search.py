from rest_framework.decorators import api_view
from rest_framework.response import Response

from slayder.models import Slayder
from tadbirlar.models import Yangiliklar
from jadidlar.models import Jadid
from hujjatlar.models import Asarlar, Maqolalar
from hikmatli_sozlar.models import Hikmatli_sozlar


@api_view(['GET'])
def full_text_search(request):
    data = request.GET.get('search', 'salom dunyo')

    return_data = {}
    objs_slider = Slayder.objects.filter(title__icontains=data).values()
    objs_yangi = Yangiliklar.objects.filter(title__icontains=data).values()
    objs_jadid = Jadid.objects.filter(fullname__icontains=data).values()
    objs_asar = Asarlar.objects.filter(title__icontains=data).values()
    objs_hikmat = Hikmatli_sozlar.objects.filter(text__icontains=data).values()
    objs_maqola = Maqolalar.objects.filter(title__icontains=data).values()


    for obj in objs_hikmat:
        if obj['jadid_id']:
            id = obj['jadid_id']
            jadid = Jadid.objects.get(id=id)
            obj['jadid_fullname'] = jadid.fullname

    return_data['slider'] = objs_slider
    return_data['yangi'] = objs_yangi
    return_data['jadid'] = objs_jadid
    return_data['asar'] = objs_asar
    return_data['hikmat'] = objs_hikmat
    return_data['maqola'] = objs_maqola

    base_url = request.build_absolute_uri('/')[:-1] + '/media/'

    for key in return_data:
        if key == 'slider':
            for obj in return_data[key]:
                # print(request.build_absolute_uri('/')[:-1])
                # print('media/')
                # print(obj['image'])
                if obj['image'] != '':
                    obj['image'] = request.build_absolute_uri('/')[:-1] + '/media/' + obj['image']
        if key == 'yangi':
            for obj in return_data[key]:
                if obj['image'] != '':
                    obj['image'] = request.build_absolute_uri('/')[:-1] + '/media/' + obj['image']
        if key == 'jadid':
            for obj in return_data[key]:
                if obj['image'] != '':
                    obj['image'] = request.build_absolute_uri('/')[:-1] + '/media/' + obj['image']
        if key == 'asar':
            for obj in return_data[key]:
                if obj['jadid_id']:
                    id = obj['jadid_id']
                    jadid = Jadid.objects.get(id=id)
                    obj['jadid_fullname'] = jadid.fullname
                if obj['image'] != '':
                    obj['image'] = request.build_absolute_uri('/')[:-1] + '/media/' + obj['image']
                if 'file' in obj and obj['file']:
                    obj['file'] = base_url + obj['file']
        if key == 'maqola':
            for obj in return_data[key]:
                if obj['jadid_id']:
                    id = obj['jadid_id']
                    jadid = Jadid.objects.get(id=id)
                    obj['jadid_fullname'] = jadid.fullname
                if obj['image'] != '':
                    obj['image'] = request.build_absolute_uri('/')[:-1] + '/media/' + obj['image']
                if 'file' in obj and obj['file']:
                    obj['file'] = base_url + obj['file']

    return Response(data=return_data)
