from rest_framework.serializers import ModelSerializer
from .models import CustomUser  , Profile
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

