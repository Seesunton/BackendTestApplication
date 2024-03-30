from django.db import models

# Create your models here.
class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=255, blank=True)  # กำหนด max_length ที่เหมาะสม
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)

def __str__(self):
    return self.Title
