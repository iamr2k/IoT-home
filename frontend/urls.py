from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/', views.linechart, name='linechart'),

]
