from urllib import response
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone, dateformat

# Create your views here.
# using generics
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary="Create new User")
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        # validating
        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(operation_summary="LogIn for User")
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        # updating last login
        user.last_login = dateformat.format(timezone.now(), "Y-m-d H:i:s")
        user.save()
        if user is not None:
            response = {"message": "Login Successfull"}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"message": "Invalid user or password"})

    @swagger_auto_schema(operation_summary="Shows Logged In User")
    def get(self, request: Request):
        if request.user.id is not None:
            content = {
                # we need to convert our values to string to show them
                "user": str(request.user),
                "id": str(request.user.id),
            }
            return Response(data=content, status=status.HTTP_200_OK)

        response = {"message": "Not logged in"}
        return Response(data=response)
