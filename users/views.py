import profile
from django.shortcuts import render
from distutils.command.upload import upload
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import pathlib
from .models import Profile
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
import json
import os
# Create your views here.


class ProfileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # user = Token.objects.get(key='e66cccb2e507c41c9b04600c4db2a889df5cb566').user

    
# 
    def get(self, request, *args, **kwargs):
    # def post(self, request, *args, **kwargs):
        print('hi')

        user = request.user

        if user:
            print("User token verified")
        else:

            print("User token not verified")



        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # token_from_req = body['token']
        # print('-'*10)
        # print(token_from_req)
        # print('-'*10)
        # self.client.force_authenticate(self.user)
        # user = Token.objects.get(key='e66cccb2e507c41c9b04600c4db2a889df5cb566').user
        # print(user)
        
        print("0"*10)
 
            
        profile = Profile.objects.get(user = user.id)
        print("profile")
        print(profile)
        serializer = ProfileSerializer(profile )

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        print('request.data : ', request.data)
        print('request.data type: ', type(request.data))
        requestDataDict = request.data.dict()
        print('requestDataDict  type: ', type(requestDataDict))

        user = request.user

        prof = Profile.objects.get(user = user.id)
        
        profile_serializer = ProfileSerializer(prof , data=request.data)

        # if profile_serializer.is_valid():

        print("hey ----->")
        # print(profile_serializer)
        # createTemp1()
        if profile_serializer.is_valid():
            print("data is valid")
            profile_serializer.save()
            
            print("created post")
            # profile_serializer.save()

            # return Response(request.data, status=status.HTTP_201_CREATED)
            print('request.data : ', request.data)
            res =     {'status':'200' , 'enty' : "hogyi bhai"  }


            print("savr ho gya post")
            return Response( res, status=status.HTTP_201_CREATED ,  content_type="application/json")

        else:
            print("error")
            print(ProfileSerializer.errors)
            print(profile_serializer.errors)
            print("data is in       valid")

            res =     {'status':'400' , 'enty' : " nhi hui hogyi bhai"  }



            return Response( res, status=status.HTTP_201_CREATED ,  content_type="application/json")

        # title = requestDataDict['title']
        # imageLocation = requestDataDict['image']

      

