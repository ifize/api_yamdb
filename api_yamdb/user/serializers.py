from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'role', 'bio'
        )


class UserEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'role', 'bio'
        )
        read_only_fields = ('role',)
