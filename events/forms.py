from django import forms
from .models import Event, Comment

class CreateEventForm(forms.ModelForm):
    """
    Form class for logged-in site
    users to create and submit an 
    event for approval by admin
    """
    class Meta:
         model = Event
         fields = [
            'title',
            'distance',
            'description',
            'image',
            'event_date',
            'event_time',
            'location',
            'max_attendees',
         ]

         widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.DateInput(attrs={'type': 'time'}),
         }

class CommentForm(forms.ModelForm):
    """
    Form class for logged-in
    users to comment on an event 
    """
    class Meta:

        model = Comment
        fields = ('text',)