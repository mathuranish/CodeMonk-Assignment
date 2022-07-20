from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    # validation
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        # User is predefined model
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        # checking is email exists
        email_exists = User.objects.filter(
            email=attrs["email"]
        ).exists()  # returns bool
        if email_exists:
            raise ValidationError("Email already in use")

        return super().validate(attrs)

    # we need to hash the user's passwords manually with this methord
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
