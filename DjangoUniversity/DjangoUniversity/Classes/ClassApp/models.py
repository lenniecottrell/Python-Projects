from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, blank=True, null=False)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60, blank=True, null=False)
    duration = models.FloatField()
    objects = models.Manager()
