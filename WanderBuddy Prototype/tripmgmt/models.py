from django.db import models

# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = models.IntegerField()
    emergencyContact = models.IntegerField()
    profilePic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
def __str__(self):
    return self.username


class Trip(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    description = models.TextField()
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    travelPlan = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    budget = models.IntegerField()
    organizer = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, blank=True)
    participants = models.ManyToManyField(Participant, related_name='trips', null=True, blank=True)

def __str__(self):
    return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='trip_images/', null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='images')


class Chatroom(models.Model):
     trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trips')
     participants = models.ManyToManyField(Participant, related_name='participants', null=True, blank=True)

class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)   
    sender = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, blank=True) 



    