from rest_framework import serializers
from .models import  newsDataFlips , newsDataNewsApi ,newsDataShorts


class newsDataSerializerShorts(serializers.ModelSerializer):
    class Meta:
        model = newsDataShorts
        fields = '__all__'


class newsDataSerializerFlips(serializers.ModelSerializer):
    class Meta:
        model = newsDataFlips
        fields = '__all__'


class newsDataSerializerNewsApi(serializers.ModelSerializer):
    class Meta:
        model = newsDataNewsApi
        fields = '__all__'
