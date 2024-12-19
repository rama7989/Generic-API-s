from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',CarsListView.as_view()),
    path('create/',CarsCreateView.as_view()),
    path('display/<int:pk>',CarsRetrieveView.as_view()),
    path('update/<int:pk>',CarsUpdateView.as_view()),
    path('delete/<int:pk>',CarsDeleteView.as_view()),
    path('lc/',CarsLCView.as_view()),
    path('ru/<int:pk>',CarsRUView.as_view()),
    path('rud/<int:pk>',CarsRUDView.as_view()),
]