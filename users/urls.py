from . import views
from django.urls import path

urlpatterns = [
    # auth urls
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    # profile and account urls
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('edit-profile/', views.editProfile, name='edit-profile'),

    # skill urls
    path('create-skill/', views.createSkill, name='create-skill'),
    path('edit-skill/<str:pk>', views.editSkill, name='edit-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),

    # messages urls
    path('inbox/', views.inbox, name='inbox')
]
