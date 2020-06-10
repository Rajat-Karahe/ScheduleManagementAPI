from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
      model = Event
      fields = ['id','url', 'title', 'event_date', 'author', 'author_name']
      read_only_fields = ['id', 'url', 'author', 'author_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']
        read_only_fields = ['id', 'url', 'username']


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

        extra_kwargs = {
        	'id': {'read_only' :  True}
        }




