from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.


from rest_framework.views import APIView
from movies.models import movie
from movies.serializers import movieserializer
from rest_framework.response import Response
from rest_framework import status

#using generic class rather than apiview
from  rest_framework import generics
class movielistcreate(generics.ListCreateAPIView):

    queryset=movie.objects.all()
    serializer_class=movieserializer
    
  

class MovieRetrievalUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=movie.objects.all()
    serializer_class=movieserializer
