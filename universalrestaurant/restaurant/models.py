from django.db import models

# Create your models here.

class Normal_Food(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title