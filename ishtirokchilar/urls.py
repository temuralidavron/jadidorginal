from django.urls import path
from .views import IshtirokchilarListCreateView#, IshtirokchilarDetailView

urlpatterns = [
    path('api/ishtirokchilar/', IshtirokchilarListCreateView.as_view(), name='ishtirokchilar-list-create'),
    # path('api/ishtirokchilar/<int:pk>/', IshtirokchilarDetailView.as_view(), name='ishtirokchilar-detail'),
]
