from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import MaxLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser


class CustomCreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all()), MaxLengthValidator(254)]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all()), MaxLengthValidator(150)]
    )
    first_name = serializers.CharField(
        validators=[MaxLengthValidator(150)]
    )
    last_name = serializers.CharField(
        validators=[MaxLengthValidator(150)]
    )
    password = serializers.CharField(
        write_only=True,
        validators=[MaxLengthValidator(150)]
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)

        return user


class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')


        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        refresh = RefreshToken.for_user(user)
        return {'auth_token': str(refresh.access_token)}
