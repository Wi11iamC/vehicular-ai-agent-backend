from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, RGBSerializer,IMU_Serializer, SemanticSerializer, RadarSerializer, LidarSerializer, DepthSerializer
from api.models import rgb_sensor, IMU_sensor, depth_camera, lidar_sensor, radar_sensor, semantic_segmentation_camera

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RGBViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = rgb_sensor.objects.all()
    serializer_class = RGBSerializer
    permission_classes = []

class IMUViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IMU_sensor.objects.all()
    serializer_class = IMU_Serializer
    permission_classes = []

class LidarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = lidar_sensor.objects.all()
    serializer_class = LidarSerializer
    permission_classes = []

class RadarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = radar_sensor.objects.all()
    serializer_class = RadarSerializer
    permission_classes = []

class DepthViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = depth_camera.objects.all()
    serializer_class = DepthSerializer
    permission_classes = []

class SemanticViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = semantic_segmentation_camera.objects.all()
    serializer_class = SemanticSerializer
    permission_classes = []