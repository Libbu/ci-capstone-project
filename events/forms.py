from django import forms
from django.core.exceptions import ValidationError
from .models import Event, Comment

class ImageTypeValidation:
   """
   Validator to check that uploaded files
   are one of .png', '.jpg', '.jpeg', '.webp',
   '.tiff', image types.
   """

   def __call__(self, value):
      if value:
        if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.tiff',)):
            raise ValidationError('Only image files are allowed.')

class CreateEventForm(forms.ModelForm):
    """
    Form class for logged-in site
    users to create and submit an 
    event for approval by admin,
    it limits the type of image
    that can be uploaded using
    the class ImageTypeValidation
    below
    """
    image = forms.ImageField(validators=[ImageTypeValidation()], required=False)

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