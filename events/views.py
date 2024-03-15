from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Event
from .forms import CreateEventForm


class EventList(generic.ListView):
    """
    Returns all the approved events in
    :model: `events.Event` and displays
    them in a page of six posts
    **Context**
    
    ``queryset``
        All approved instances of :model: `events.Event`
    ``paginate_by``
        Number of events per page.
    
    **Template**

    :template: `events/event_list.html`
    """
    queryset = Event.objects.filter(approved = True)
    template_name = "events/event_list.html"
    paginate_by = 6


def create_event(request):
    """
    Users who have registered and logged in
    can create an event with the CreateEventForm
    using fields from :model: `events.Event`.
    The event must be approved by a site-admin
    (superuser) before showing in event_list.html
    """
    if request.method == 'POST':
        event_form = CreateEventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.creator = request.organiser
            event.save()

            messages.success(request, "Your run has been submitted and is awaiting admin approval.")

            return redirect('EventList')
    else:
        event_form = CreateEventForm()

    return render(request, 'events/create_event.html', {'event_form': event_form})
