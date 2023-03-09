from django.shortcuts import render
from rest_framework import viewsets
from .models import Establishments, Category, QA
from .serializers import EstablishmentsSerializer, CategorySerializer, QASerializer

# Create your views here.

class EstablishmentsViewSet(viewsets.ModelViewSet):
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QAViewSet(viewsets.ModelViewSet):
    queryset = QA.objects.all()
    serializer_class = QASerializer