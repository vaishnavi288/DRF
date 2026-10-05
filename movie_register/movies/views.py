from django.shortcuts import render
# Create your views here.


from rest_framework.views import APIView
from movies.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)