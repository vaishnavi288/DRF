from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.


from rest_framework.views import APIView
from movies.models import movie
from movies.serializers import movieserializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


    
#search apiview


class searchapiview(APIView):
    def get(self,request):

        #fetch data coming from the request url
        data=self.request.query_params.get('search')

        #filter movie record having title matching
        m=movie.objects.filter(Q(title__icontains=data)| Q(director__icontains=data)| Q(language__icontains=data))

        if not m.exists():
            return Response({"message":"no record found"},status=status.HTTP_200_OK)

        serializer_instance=movieserializer(m,many=True)

        return Response(serializer_instance.data,status=status.HTTP_200_OK)


#using filter method
from rest_framework import generics
from rest_framework.filters import SearchFilter

class searchapiview(generics.ListAPIView):
    queryset=movie.objects.all()

    serializer_class=movieserializer
    filter_backends=[SearchFilter]
    search_fields=['title','director','language']




