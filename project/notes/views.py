from django.shortcuts import render

# Create your views here.

#Default

from .models import Note
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt



#Viewsets
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from datetime import date

class NoteViewSet(viewsets.ModelViewSet):
	serializer_class = NoteSerializer
	queryset = Note.objects.all()


