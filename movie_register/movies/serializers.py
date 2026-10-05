from rest_framework import serializers

from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name'
        ]
#to create user account we user uder.objects.create_user not create ,for password hashing
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        return u