from django.db import models

# Create your models here.
class rgb_sensor(models.Model):
    timestamp = models.IntegerField()
    image_url=models.ImageField(upload_to='rgb_images')

class semantic_segmentation_camera(models.Model):
    timestamp = models.IntegerField()
    image_url = models.ImageField(upload_to = "semantic_segmentation_images")

class depth_camera(models.Model):
    timestamp = models.IntegerField()
    image_url = models.ImageField(upload_to = "depth_camera_images")

class collision_detector(models.Model):
    timestamp = models.IntegerField()


class GNSS_sensor(models.Model):
    timestamp = models.IntegerField()

class lane_invasion_detector(models.Model):
    timestamp = models.IntegerField()
    
class lidar_sensor(models.Model):
    timestamp = models.IntegerField()

class obstacle_detector(models.Model):
    timestamp = models.IntegerField()

class radar_sensor(models.Model):
    timestamp = models.IntegerField()

class rss_sensor(models.Model):
    timestamp = models.IntegerField()

class IMU_sensor(models.Model):
    timestamp = models.IntegerField()

class semantic_lidar_sensor(models.Model):
    timestamp = models.IntegerField

class instance_segmentation_camera(models.Model):
    timestamp = models.IntegerField

class DVS_camera(models.Model):
    timestamp = models.IntegerField

class optical_flow_camera(models.Model):
    timestamp = models.IntegerField

class IMU_sensor(models.Model):
    timestamp = models.IntegerField()
    accelerometer = models.IntegerField()
