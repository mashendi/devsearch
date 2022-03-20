from . import views
from django.urls import path

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile')
]
