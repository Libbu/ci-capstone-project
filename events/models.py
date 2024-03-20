from django.db import models
from django.contrib.auth.models import User
from datetime import date 
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
    """
    Stores a single event related 
    to :model: `auth.User` through the use
    of CreateEventForm in forms.py
    """
    title = models.CharField(max_length=200)
    distance = models.CharField(max_length = 20)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_organiser")
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=200)
    attendees  = models.ManyToManyField(User, related_name = 'attendees', blank=True)
    max_attendees = models.PositiveIntegerField('maximum_attendees', default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"{self.title} | created by {self.organiser}"
    
    @property
    def days_until (self):
        """
        calculates how many days left
        until the run is due to take place
        """
        today = date.today()
        days_left = self.event_date - today
        days_left_date = str(days_left).split(",",1)[0]
        return days_left_date
    
    @property
    def is_past (self):
        today = date.today()
        if self.event_date < today:
            timing = "past"
        else:
            timing = "future"
        return timing