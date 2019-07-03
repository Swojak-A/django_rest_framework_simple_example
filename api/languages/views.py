from django.shortcuts import render
from rest_framework import viewsets

from .models import Language
from .serializers import LanguageSerializer

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
	# takes cares of most common endpoints of REST api

	queryset = Language.objects.all()
	serializer_class = LanguageSerializer