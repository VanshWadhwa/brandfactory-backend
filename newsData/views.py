from .serializers import newsDataSerializerFlips , newsDataSerializerShorts , newsDataSerializerNewsApi
from .models import  newsDataFlips , newsDataNewsApi ,newsDataShorts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class newsDataShortsViews(APIView):

    def get(self, request, id=None):
        if id:
            item = newsDataShorts.objects.get(id=id)
            serializer = newsDataSerializerShorts(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = newsDataShorts.objects.all()
        serializer = newsDataSerializerShorts(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class newsDataFlipsViews(APIView):

    def get(self, request, id=None):
        if id:
            item = newsDataFlips.objects.get(id=id)
            serializer = newsDataSerializerFlips(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = newsDataFlips.objects.all()
        serializer = newsDataSerializerFlips(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class newsDataNewsApiViews(APIView):

    def get(self, request, id=None):
        if id:
            item = newsDataNewsApi.objects.get(id=id)
            serializer = newsDataSerializerNewsApi(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = newsDataNewsApi.objects.all()
        serializer = newsDataSerializerNewsApi(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
