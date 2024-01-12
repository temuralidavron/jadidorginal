from django.urls import path

from manbalar.views import VideolarListCreateView, RasmlarListCreateView, AudiolarListCreateView

urlpatterns = [
    path('api/videolar/', VideolarListCreateView.as_view(), name='videolar-list-create'),
    # path('api/videolar/<int:pk>/', VideolarDetailView.as_view(), name='videolar-detail'),

    path('api/rasmlar/', RasmlarListCreateView.as_view(), name='rasmlar-list-create'),
#     path('api/rasmlar/<int:pk>/', RasmlarDetailView.as_view(), name='rasmlar-detail'),

    path('api/audiolar/', AudiolarListCreateView.as_view(), name='audiolar-list-create'),
#     path('api/audiolar/<int:pk>/', AudiolarDetailView.as_view(), name='audiolar-detail'),
]
