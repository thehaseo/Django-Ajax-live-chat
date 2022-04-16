from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True, blank=True)
    user = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)