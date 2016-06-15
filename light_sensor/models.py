from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class SensorData(models.Model):
    entry_id = models.IntegerField(default=0)
    light_value = models.IntegerField(default=0)
    temp_value = models.FloatField(default=0)
    alert_value = models.IntegerField(default=300)
    tel = models.CharField(max_length=20, default='0802618207')

    def __str__(self):
        return self.entry_id
