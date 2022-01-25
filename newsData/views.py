from .serializers import newsDataSerializer
from .models import newsData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class newsDataViews(APIView):

    def get(self, request, id=None):
        if id:
            item = newsData.objects.get(id=id)
            serializer = newsDataSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = newsData.objects.all()
        serializer = newsDataSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
