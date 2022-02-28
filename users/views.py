from functools import partial
import imp
from django.shortcuts import render
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser


class ProfileViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    # def list(self , request):
    #     prof = Profile.objects.all()
    #     serializers = ProfileSerializer(prof , many = True)
    #     return Response(serializers.data)

    def retrieve(self , request , pk=None):
        id = request.user.id
        if id is not None:
            prof = Profile.objects.get(id = id)
            serializer = ProfileSerializer(prof)
            return Response(serializer.data)
    
    def update(self , request , pk):
        id = request.user.id
        prof = Profile.objects.get(pk = id)
        serializer = ProfileSerializer(prof  , data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : 'Complete Data Updated'})
        print(serializer.errors)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

        
    def partial_update(self , request , pk):
        id = pk
        prof = Profile.objects.get(pk = id)
        serializer = ProfileSerializer(prof  , data = request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : 'Complete Data Updated'})
        print(serializer.errors)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)