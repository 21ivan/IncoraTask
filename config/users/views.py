from django.shortcuts import render
from rest_framework import generics
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import User


# Create your views here.

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Message': 'User created successfully',
                'User': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'Errors': serializers.as_serializer_error}, status=status.HTTP_400_BAD_REQUEST)


class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
