from django.contrib.auth.models import User
from api.models import rgb_sensor, IMU_sensor, depth_camera, semantic_segmentation_camera, lidar_sensor, radar_sensor
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class RGBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rgb_sensor
        fields = ['image_url']

class IMU_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IMU_sensor
        fields = ['image_url']

class LidarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lidar_sensor
        fields = ['image_url']
    
class RadarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = radar_sensor
        fields = ['image_url']

class DepthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = depth_camera
        fields = ['image_url']

class SemanticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = semantic_segmentation_camera
        fields = ['image_url']