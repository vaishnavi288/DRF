from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
# Create your views here.
from django.shortcuts import get_object_or_404
from employees.models import employee

from rest_framework.views import APIView
from rest_framework.response import Response
from employees.serializers import employeeSerializer
#APIview for reading all employee records
class employeelist(APIView):
    def get(self,request):
        
        data = employee.objects.all()

        #reads all employee records from db table(return format is qs)

        serializer_instance=employeeSerializer(data,many=True)

        #employeeSerializer converts qs into python native types
        #qs contains more than one records so we use many=true

        return Response(data=serializer_instance.data)
        #send python native data as json using response class




import json

#APIview for creating a new employee records

class employeecreate(APIView):

    def post(self, request):

    # view recieve data as request.data
    # calla serializer class for deserialization.here we pass request.data as arguments
    # after validation serializer saves  data as model object inside db table



        # data = json.loads(request.body)

        # data=request.data  #python native

        # e = data['empid']
        # n = data['name']
        # a = data['age']
        # p = data['place']
        # g = data['gender']
        # j = data['joining_date']
        # s = data['salary']
        # d = data['designation']

        # employee.objects.create(
        #     empid=e,
        #     name=n,
        #     age=a,
        #     place=p,
        #     gender=g,
        #     joining_date=j,
        #     salary=s,
        #     designation=d
        # )

        serializer_instance=employeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
            

        

        # employee.objects.create(**data)

       
#apiview for reading specific record

class employeeretrieve(APIView):

    def get(self, request, i):

        #reads employee object from model
        # e = (employee.objects.get(id=i))
        e=get_object_or_404(employee,id=i)

        # convert model object into python native using employeeserializer
       
        serializer_instance=employeeSerializer(e)

       
       
    #    sends the response as json us
        return Response(serializer_instance.data)

 

# apiview for updating existing record fullupdation
class employeefullupdate(APIView):

    def put(self, request, i):

        e = employee.objects.get(id=i)
        serializer_instance=employeeSerializer(e,request.data,)
        if serializer_instance.is_valid():
            serializer_instance.save()  #calls update()inside serializer class


        # data = json.loads(request.body)

        # try:
        #     e = employee.objects.get(id=i)

        #     e.empid = data['empid']
        #     e.name = data['name']
        #     e.age = data['age']
        #     e.place = data['place']
        #     e.gender = data['gender']
        #     e.joining_date = data['joining_date']
        #     e.salary = data['salary']
        #     e.designation = data['designation']

        #     e.save()

            return Response({
                "message": "employee updated successfully"
            })

        else:
            return Response(serializer_instance.errors)

        # except:
        #     return Response({
        #         "message": "no employee data"
        #     })



class employeepartialupdate(APIView):

    def patch(self, request, i):

        e = employee.objects.get(id=i)
        serializer_instance=employeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                        "message": "employee updated successfully"
                         })
                    
        else:
                                
                                
             return Response(serializer_instance.errors)







#         data = json.loads(request.body)

#         try:
#             e = employee.objects.get(id=i)

#             if 'empid' in data:
#                 e.empid = data['empid']

#             if 'name' in data:
#                 e.name = data['name']

#             if 'age' in data:
#                 e.age = data['age']

#             if 'place' in data:
#                 e.place = data['place']

#             if 'gender' in data:
#                 e.gender = data['gender']

#             if 'joining_date' in data:
#                 e.joining_date = data['joining_date']

#             if 'salary' in data:
#                 e.salary = data['salary']

#             if 'designation' in data:
#                 e.designation = data['designation']

#             e.save()

#             return Response({
#                 "message": "employee partially updated"
#             })

#         except:
#             return Response({
#                 "message": "no employee data"
#             })


# # apiview for delecting specific record
class employeedelete(APIView):

    def delete(self, request, i):

     
            e = get_object_or_404(employee,id=i)
            e.delete()

            return Response({
                "message": "employee deleted successfully"
            })

       

