from rest_framework import serializers

from .utils import simple_auth_usercus
from .models import UserCus

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCus
        fields = ['email', 'username', 'fullname', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return UserCus.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Sử dụng username và password để xác thực
        user = simple_auth_usercus(username=data['username'], password=data['password'])

        if user:
            return user
        raise serializers.ValidationError("Invalid credentials")
