from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile')
]
