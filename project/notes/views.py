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


'''

from rest_framework.views import APIView

class NoteAPIView(APIView):
	def get(self,request):
		notes = Note.objects.all()
		serializer = NoteSerializer(notes,many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer=NoteSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class NoteDetails(APIView):
	def get_object(self,id):
		try:
			note = Note.objects.get(id=id)
		except Note.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	def get(self,request,id):
		note=self.get_object(id)
		serializer = NoteSerializer(note)
		return Response(serializer.data)
		
	def put(self,request,id):
		note=self.get_object(id)
		serializer=NoteSerializer(note, data=request.data)

		if serializer.is_valid():
			serializer.last_updated_date=datetime.now()
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id):
		note=self.get_object(id)
		note.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

'''