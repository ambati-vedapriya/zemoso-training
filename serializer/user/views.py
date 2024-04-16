from django.shortcuts import render
from rest_framework.views import  APIView
from django.http import HttpResponse
from rest_framework.response import Response

from .exceptions import UserNotFoundException

from .utils import encrypt_password
from .serializer import UserResponse,UserRequest
from .models import User
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

def is_existing_user(id):
        existing_User=User.objects.filter(id = id).first()
        if not existing_User:
            raise UserNotFoundException(f"user not found {id}")
        return existing_User 

class UserDetailView(APIView):
    def get(self ,request,id ):
        user=is_existing_user(id)
        return Response(UserResponse(user).data)

    def delete(self,request,id):
        existing_User=is_existing_user(id)
        existing_User.delete()
        return Response({"msg":"deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["name", "email", "password"],
        ),
        operation_description="Retrieve user by ID",
        manual_parameters=[
            openapi.Parameter(
                "id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="User ID",
            ),
        ],
    )

    def put(self,request,id):
        existing_User=is_existing_user(id)
        user_req = UserRequest(instance=existing_User, data=request.data,partial=True)
        if user_req.is_valid():
            user_req.save()
            return Response({"msg":"updateed sucessfully"},status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'updated successfully', 'details': user_req.errors},status=status.HTTP_204_NO_CONTENT)

        
        

class UserListView(APIView):

    @swagger_auto_schema(responses={200: UserResponse(many=True)})
    


    def get(self,request):
        users=User.objects.all()
        return Response(UserResponse(users,many=True).data)
    
    @swagger_auto_schema(responses={200: UserResponse(many=True)},request_body=UserRequest)

    def post(self, request):
        user_req = UserRequest(data=request.data)
        
        if user_req.is_valid():
            existing_user = User.objects.filter(email=user_req.validated_data.get('email')).first()
            
            if existing_user:
                raise UserNotFoundException(f"user already exits")

            user_req.validated_data['password'] = encrypt_password(user_req.validated_data.get('password'))
            user_response = user_req.save()

            return Response(UserResponse(user_response).data)

        # Return validation errors in case of failure
        return Response({'error': 'Validation failed', 'details': user_req.errors}, status=400)

   