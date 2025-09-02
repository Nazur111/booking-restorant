from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'room_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Place(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
   


class Booking(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()