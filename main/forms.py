from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import MainAbout

class MainAboutForm(forms.ModelForm):
    """
    Form class for site superusers to
    update the about our community section 
    on the index.html page
    """
    class Meta:
        model = MainAbout
        fields = ['content',]
        widgets = {
            'content': SummernoteWidget(),
        }