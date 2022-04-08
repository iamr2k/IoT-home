from django.db import models

# Create your models here.

class temp_log(models.Model):
    temp= models.FloatField()
    humidity = models.FloatField()
    time = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.temp