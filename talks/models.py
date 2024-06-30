from django.db import models

class Talk(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    recorded_date = models.CharField(max_length=1024, null=True, blank=True)
