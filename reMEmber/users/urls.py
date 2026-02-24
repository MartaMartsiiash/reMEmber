"""
URL configuration for user-related views.
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_redirect),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
]
