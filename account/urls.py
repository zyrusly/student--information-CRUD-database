from django.urls import path, include
from .views import ProfileCreateView,ProfileUpdateView,ProfileDeleteView,ProfileDetailView
from django.urls import reverse
from .views import profile_queryset as p_query

urlpatterns = [
    path('', p_query, name='profile_query'),
    path('new/', ProfileCreateView.as_view( success_url='/accounts/'), name='profile_create'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('<int:pk>/update/', ProfileUpdateView.as_view( success_url='/accounts/'), name='profile_update'),
     path('<int:pk>/delete/', ProfileDeleteView.as_view( success_url='/accounts/'), name='profile_delete'),
]
