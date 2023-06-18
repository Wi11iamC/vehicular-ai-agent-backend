from django.contrib.auth.models import User
from api.models import rgb_sensor
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class RGBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rgb_sensor
        fields = ['image_url']