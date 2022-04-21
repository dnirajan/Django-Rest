from .serializer import *
from .models import *
from rest_framework import viewsets
from django.shortcuts import render


#for all crud operations
class SingerViewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class= SingerSerializer
    
class SongViewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer