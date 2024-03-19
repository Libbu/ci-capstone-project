from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MainAbout
from .forms import MainAboutForm

# Create your views here.
def home_view(request):
    """
    this view returns the most recent
    instance of :model: MainAbout to the
    'about our community'section of the homepage
    using the template main/index.html
    """
    home = MainAbout.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "main/index.html",{'home': home})

@login_required
def admin_update_about(request):
    """
    For use by site admin to update
    the about section of the website
    homepage

    """
    if not request.user.is_superuser:
        return render(request, 'prohibited.html')
    
    if request.method == 'POST':
        about_form = MainAboutForm(request.POST)
        if about_form.is_valid():
            about = about_form.save(commit=True)
            about.save()

            messages.success(request, "Your update to the homepage has been published") 
    
    form = MainAboutForm()

    return render(
        request, 
        'main/update_about.html',
        {'form': form,
        },
    )
 
