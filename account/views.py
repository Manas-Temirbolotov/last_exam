from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Author
from .serializers import AuthorRegisterSerializer


class AuthorRegisterView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    authentication_classes = [TokenAuthentication, ]
