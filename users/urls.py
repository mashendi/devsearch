from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit-profile/', views.editProfile, name='edit-profile'),

    path('create-skill/', views.createSkill, name='create-skill')
]
