from rest_framework import serializers
from .models import newsData


class newsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsData
        fields = '__all__'
