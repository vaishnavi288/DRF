from django.db import models

# Create your models here.
class employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)

    gender_choices=[

        ('male','Male'),('female','Female')    #data value  display value
    ]

    gender=models.CharField(max_length=20,choices=gender_choices)


    joining_date=models.DateField()
    # joining_date=models.DateField(auto_now_add=True) current time will save


    salary=models.IntegerField()
    designation=models.CharField(max_length=30)


    image=models.ImageField(upload_to='employee',null=True)
