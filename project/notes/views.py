from django.shortcuts import render

# Create your views here.

#Default

from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt



#Viewsets
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

#Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


from datetime import date

class NoteViewSet(viewsets.ModelViewSet):
	permission_classes=(IsAuthenticated,)
	authentication_classes = (BasicAuthentication,)
	serializer_class = NoteSerializer
	queryset = Note.objects.all()


