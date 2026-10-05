from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

#apiview for reading all records
from rest_framework.views import APIView
from movies.models import movie
from movies.serializers import movieserializer
from rest_framework.response import Response
from rest_framework import status
class movielist(APIView):
    def get(self,request):
        m=movie.objects.all()
        serializer_instance=movieserializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


#apiviw for creating a new record
class moviecreate(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=movieserializer(data=form_data,)
        if serializer_instance.is_valid():


            # data afte validation
            # cleaned_data=serializer_instance.validated_data
            # title=cleaned_data['title']  #if we want to display title we do the above and this line
            
            
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)






# apivie for reading specific record,full updation, partial updation  and delete in single class

class movieretrivalupdatedelete(APIView):
    def get(self,request,i):
        m=get_object_or_404(movie,id=i)
        serializer_instance=movieserializer(m)
        return Response(serializer_instance.data)


    def put(self,request,i):

        form_data=request.data
        m=movie.objects.get(id=i)
        serializer_instance=movieserializer(m,data=form_data)
        if serializer_instance.is_valid():
             serializer_instance.save()
             return Response(serializer_instance.data)
        else:
             return Response(serializer_instance.errors)
        


    def patch(self,request,i):
            
       form_data=request.data
       m=movie.objects.get(id=i)
       serializer_instance=movieserializer(m,data=form_data,partial=True)
       if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
       else:
             return Response(serializer_instance.errors)


    def delete(self,request,i):

        m=get_object_or_404(movie,id=i)
        m.delete()
        return Response({"message":"deleted"})

