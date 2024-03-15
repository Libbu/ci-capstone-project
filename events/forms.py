from django import forms
from .models import Event

class CreateEventForm(forms.ModelForm):
    """
    Form class for logged-in site
    users to create and submit an 
    event for approval by admin"
    """
    class Meta:
         model = Event
         fields = ()
