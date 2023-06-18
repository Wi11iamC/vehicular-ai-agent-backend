from django.db import models

# Create your models here.
class rgb_sensor(models.Model):
    image_url=models.ImageField(upload_to='rgb_images')
