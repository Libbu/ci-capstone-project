from django.shortcuts import render
from .models import MainAbout

# Create your views here.
def home_view(request):
    """
    this view returns the most recent instance
    of :model: MainAbout to the 'about our community'
    section of the homepage using the template main/index.html
    """
    home = MainAbout.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "main/index.html",{'home': home})