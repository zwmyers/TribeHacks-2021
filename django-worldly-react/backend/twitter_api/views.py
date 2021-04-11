from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TwitterSerializer
from .models import Twitter

# Create your views here.

class TwitterView(viewsets.ModelViewSet):
    serializer_class = TwitterSerializer
    queryset = Twitter.objects.all()
