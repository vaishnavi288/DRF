
from rest_framework import serializers
from employees.models import employee  
class employeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    place=serializers.CharField(max_length=30)

    gender_choices=[

        ('male','Male'),('female','Female')    #data value  display value
    ]

    gender=serializers.ChoiceField(choices=gender_choices)


    joining_date=serializers.DateField()
    # joining_date=models.DateField(auto_now_add=True) current time will save


    salary=serializers.IntegerField()
    designation=serializers.CharField()
    image=serializers.ImageField()



#after validation and before saving

    def create(self,validated_data):
        e=employee.objects.create(**validated_data)
        return e  #return employee object

#after validation and before saving

    def update(self,instance,validated_data):
        instance.empid=validated_data.get('empid',instance.empid) #if the given data doest have this data then i.empid is assigned which is the data before updation
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.salary=validated_data.get('salary',instance.salary)
        instance.place=validated_data.get('place',instance.place)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.designation=validated_data.get('designation',instance.designation)
        instance.joining_date=validated_data.get('joining_date',instance.joining_date)
        instance.save()
        return instance