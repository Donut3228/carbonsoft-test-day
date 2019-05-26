from django.db import models



class Sensor(models.Model):
    
    name = models.CharField(max_length=100)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):

        return self.name



class SensorHistory(models.Model):

    date = models.DateTimeField(auto_now_add=True, blank=True)
    value = models.CharField(max_length=400)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_history')
    


# hardware_names = ['CPU', 'Memory', 'Disks', 'Network', 'CPU temp', ]

# Create your models here.
