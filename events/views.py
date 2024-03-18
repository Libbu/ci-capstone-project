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
    queryset = Event.objects.filter(approved=True)
    template_name = "events/event_list.html"
    paginate_by = 6

def event_detail(request, event_id):

    queryset = Event.objects.filter(approved=True)
    event = get_object_or_404(queryset, event_id=event_id)

    return render(
        request,
        'events/event_detail.html', {'events': event},
    )


@login_required
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
            event.organiser = request.user
            event.save()

            messages.success(request, "Your event has been submitted and is awaiting approval.") 
    
    form = CreateEventForm()

    return render(
        request, 
        'events/create_event.html',
        {'form': form,
        },
    )
#admin event approval page

@login_required
def admin_event_approval_list(request):
    """
    For use by site admin who can see 
    which events need approval

    """
    pending_events = Event.objects.filter(approved=False).order_by('-event_date')

    if not request.user.is_superuser:
        return render(request, 'prohibited.html')

 
    return render(request, 'events/admin_event_approval.html', {'pending_events': pending_events,})


@login_required
def admin_event_approval(request, event_id):

    pending_events = Event.objects.filter(approved=False).order_by('-event_date')

    if not request.user.is_superuser:
        return render(request, 'prohibited.html')

    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'approve':
            event.approved = True
            event.save()
            messages.success(request, f'Event {event.title} has been approved.')

        elif action == 'decline':
            event.delete()
            messages.success(request, 'Event has been declined and deleted.')

    return render(request, 'events/admin_event_approval.html',{'pending_events': pending_events,},)



    
    
