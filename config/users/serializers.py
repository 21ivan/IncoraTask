# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, args):
        email = args.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'username already exists'})
        return super().validate(args)
