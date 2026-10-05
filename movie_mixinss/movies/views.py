from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

#apiview for reading all records
from rest_framework.views import APIView
from movies.models import movie
from movies.serializers import movieserializer
from rest_framework.response import Response
from rest_framework import status

#using mixin class rather than apiview
from  rest_framework import mixins,generics
class movielist(mixins.ListModelMixin,generics.GenericAPIView):

    queryset=movie.objects.all()
    serializer_class=movieserializer

    def get(self,request):
        return self.list(request)
    
class moviecreate(mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=movie.objects.all()
    serializer_class=movieserializer
    
    def post(self,request):
        return self.create(request)

class MovieRetrievalUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=movie.objects.all()
    serializer_class=movieserializer
    def get(self,request,pk):
            return self.retrieve(request,pk)
    def put(self,request,pk):
            return self.update(request,pk)
    def patch(self,request,pk):
            return self.partial_update(request,pk)
    def delete(self,request,pk):
            return self.destroy(request,pk)