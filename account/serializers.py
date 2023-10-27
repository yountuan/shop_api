from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model
from .utils import send_activation_code


User = get_user_model()


class RegisterSerializer(ModelSerializer):
    password_confirm = CharField(min_length=5, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'email', 'password', 'password_confirm'

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise ValidationError('password do not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


