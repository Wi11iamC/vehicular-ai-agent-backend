from django.db import models

# Create your models here.

class rgb_sensor(models.Model):
    image_url=models.ImageField(upload_to='rgb_images')

class semantic_segmentation_camera(models.Model):
    image_url = models.ImageField(upload_to = "semantic_segmentation_images")

class depth_camera(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class collision_detector(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")


class GNSS_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class lane_invasion_detector(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")
    
class lidar_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class obstacle_detector(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class radar_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class rss_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")


class semantic_lidar_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class instance_segmentation_camera(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class DVS_camera(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class optical_flow_camera(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")

class IMU_sensor(models.Model):
    image_url = models.ImageField(upload_to = "depth_camera_images")
    accelerometer = models.IntegerField()
    gyroscopeX = models.IntegerField()
    gyroscopeY = models.IntegerField()