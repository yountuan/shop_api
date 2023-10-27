from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully registered', status=201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User is not found', status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Activated', status=200)
