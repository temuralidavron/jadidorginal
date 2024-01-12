from django.urls import path
from .views import Foydali_havolalarListCreateView#, Foydali_havolalarDetailView

urlpatterns = [
    path('api/foydali_havolalar/', Foydali_havolalarListCreateView.as_view(), name='foydali_havolalar-list-create'),
    # path('api/foydali_havolalar/<int:pk>/', Foydali_havolalarDetailView.as_view(), name='foydali_havolalar-detail'),
]
