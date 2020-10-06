from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('f/<str:filename>/', views.File, name='File'),
]