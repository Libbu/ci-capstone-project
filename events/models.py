from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_organiser")
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    max_attendees = models.PositiveIntegerField('Maximum Attendees', default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"{self.title} | created by {self.organiser}"