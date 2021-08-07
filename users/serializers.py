from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegistrationUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        max_length=254,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.SlugField(
        required=False,
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())])

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep.pop('username', None)
        return rep

    class Meta:
        fields = ('email', 'username')
        model = User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email',
                  'role')
        model = User
        lookup_field = 'username'
