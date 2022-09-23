from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile2, name='profile'),
]
