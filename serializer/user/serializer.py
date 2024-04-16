

from rest_framework import serializers

from .models import User
 

class UserRequest(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, min_length=3)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, min_length=8)

    class Meta:
        model=User
        fields=('name','email','password')
        
class UserResponse(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('id','name','email')