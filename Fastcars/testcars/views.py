from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class CarsListView(ListAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsCreateView(CreateAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsRetrieveView(RetrieveAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsUpdateView(UpdateAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsDeleteView(DestroyAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

# list viewTypes

class CarsLCView(ListCreateAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsRUView(RetrieveUpdateAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer

class CarsRUDView(RetrieveUpdateDestroyAPIView):
    queryset=CarsModel.objects.all()
    serializer_class=CarSerializer