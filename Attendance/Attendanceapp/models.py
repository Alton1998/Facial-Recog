from django.db import models

# Create your models here.
class StartAttendance(models.Model):
    Update=models.CharField(max_length=3)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.Update,self.time
class Present(models.Model):
    Name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)