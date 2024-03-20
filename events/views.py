from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Event
from .forms import CreateEventForm


class EventList(LoginRequiredMixin, generic.ListView):
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

def event_detail(request, id):

    queryset = Event.objects.filter(approved=True)
    event = get_object_or_404(queryset, id=id)

    return render(
        request,
        'events/event_detail.html', {'event': event},
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


@login_required
def user_events(request):
    """
    this view serves the user a 
    list of all events they have created
    **Context**
    
    All instances of :model: `events.Event`
    created by the request.uer
    
    **Template**

    :template: `events/user_events.html`
    """

    events = Event.objects.filter(organiser=request.user) 

    return render(request, 'events/user_events.html', {'events':events})


@login_required
def admin_event_approval_list(request):
    """
    For use by site admin (superusers)
    to see events pending approval

    """
    pending_events = Event.objects.filter(approved=False).order_by('-event_date')

    if not request.user.is_superuser:
        return render(request, 'prohibited.html')

 
    return render(request, 'events/admin_event_approval.html', {'pending_events': pending_events,})


@login_required
def admin_event_approval(request, event_id):
    """
    updates the database with the decision
    of the admins, if they push the approved
    button in admin_event_approval.html then
    the event will show on the event_list for
    all logged in users; if they decline the
    event it will be deleted.
    """

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

    return HttpResponseRedirect(reverse('admin_event_approval'))



@login_required
def delete_event(request, event_id):
    """
    allows a logged in user to delete
    their own event in the event_detail.
    """

    event = get_object_or_404(Event, pk=event_id,)
    if request.user == event.organiser:
        event.delete()
        messages.success(request, f"Event successfully deleted")

    return HttpResponseRedirect(reverse('user_events'))

@login_required
def update_event(request, event_id):
    """
    allows a logged in user to delete
    their own event by clicking on update
    in the event detail. They will be taken
    to update_event.html which will prepopulate
    with the details of the event they wish to
    update
    """

    event = get_object_or_404(Event, pk=event_id,)
    if request.user == event.organiser:
        if request.method == 'POST':
            form = CreateEventForm(request.POST, instance=event)
            if form.is_valid():
                form.save(commit=False)
                event.organiser = request.user
                event.save()
                return HttpResponseRedirect(reverse('user_events'))
        else:
            form = CreateEventForm(instance=event)
        return render(request, 'events/update_event.html', {'form': form})

@login_required
def attend_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if event.max_attendees == 0 or event.attendees.count() < event.max_attendees:
		if request.method == 'POST':
			event.attendees.add(request.user)
			return render(
            request,
            'events/event_detail.html', {'event': event},
            )
	else:
		messages.success(request, "Sorry, this run is full")
	return redirect('event-list')

@login_required
def cancel_attendance(request, event_id):
    """
    allows users to remove themselves
    from an event they have said they
    will attend
    """
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
	    event.attendees.remove(request.user)
	    return redirect('event_list')
    
