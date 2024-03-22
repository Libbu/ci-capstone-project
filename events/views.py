from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from .models import Event, Comment
from .forms import CreateEventForm, CommentForm


class EventList(LoginRequiredMixin, generic.ListView):
    """
    Returns all the approved, future events in
    :model: `events.Event` and displays
    them in a page of six posts
    **Context**
    
    ``queryset``
        All approved, future events relative to today
        instances of :model: `events.Event`
    ``paginate_by``
        Number of events per page.
    
    **Template**

    :template: `events/event_list.html`
    """
    model = Event
    template_name = "events/event_list.html"
    paginate_by = 6
    
    def get_queryset(self):
        queryset = Event.objects.filter(approved=True)
        today = timezone.now().date()
        queryset = queryset.filter(event_date__gte=today)

        return queryset

@login_required
def event_detail(request, id):

    """ 
    Displays an individual instance of
    :model: `events.Event`

    **Context**
    ``event``
    an instance of :model: `events.Event`
    ``comments``
    all comments related to the event

    **Template**
    :template: `events/event_detail.html`
    """

    queryset = Event.objects.all()
    event = get_object_or_404(queryset, id=id)
    comments = event.comments.all().order_by("-created_on")

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment published'
            )

    comment_form = CommentForm()

    return render(
        request,
        'events/event_detail.html', {'event': event, "comments": comments,"comment_form": comment_form, },
    )

@login_required
def delete_comment(request, event_id, comment_id):

    """
    A user can delete their own comment, superusers
    can delete any comments.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``comment``
        A single comment related to the event.
    """

    queryset = Event.objects.filter(approved = True)
    event = get_object_or_404(queryset, id=event_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect('event_detail', id=event_id)

@login_required
def edit_comment(request, event_id, comment_id):
    """
    Displays a comment for edit by the user
    who made it in the CommentForm.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``comment``
        A single comment related to the event.
    ``comment_form``
        An instance of :form:`events.CommentForm`
    """

    if request.method == "POST":

        queryset = Event.objects.filter(approved = True)
        event = get_object_or_404(queryset, id=event_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment')

    return redirect('event_detail', id=event_id)

@login_required
def create_event(request):
    """
    Users who have registered and logged in
    can create an event with the CreateEventForm
    using fields from :model: `events.Event`.
    The event must be approved by a site-admin
    (superuser) before showing in event_list.html
    
    **Context**
    ``EventCreateForm``
    an instance of `:form: events.EventCreateForm`

    **Template**
    :template: `create_event.html`
    """
  
    if request.method == 'POST':
        event_form = CreateEventForm(request.POST, request.FILES)
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

    current_date = timezone.now().date()
    events = Event.objects.filter(organiser=request.user) 

    return render(request, 'events/user_events.html', {'events':events, 'current_date':current_date,})

@login_required
def admin_event_approval_list(request):
    """
    For use by site admin (superusers)
    to see events pending approval

    **Context**

    ``pending_Event``
        instances of :model:`events.Event`
        where approved = False.
    
    **Template**

    :template: `admin_event_approval.html`

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
            messages.success(request, 'Event has been declined and removed.')

    return HttpResponseRedirect(reverse('admin_event_approval'))

@login_required
def delete_event(request, event_id):
    """
    allows a logged in user to delete
    their own event in the event_detail
    
    also alows a superuser to delete any
    event from the event_detail.
    """

    event = get_object_or_404(Event, pk=event_id,)
    if request.user == event.organiser or request.user.is_superuser:
        event.delete()
        messages.success(request, f"Event successfully deleted.")

    return HttpResponseRedirect(reverse('user_events'))

@login_required
def update_event(request, event_id):
    """
    allows a logged in user to update
    their own event by clicking on update event
    in the event_detail. They will be taken
    to update_event.html which will prepopulate
    with the details of the event they wish to
    update

    the event will be resubmitted for admin
    approval after being updated.

    **Context**

    ``event``
        An instance of :model:`events.Event`.
    ``EventCreateForm`
        An instance of :form:`events.EventCreateForm`
    **Template**

    :template: `update_event.html`
    """
    
    event = get_object_or_404(Event, pk=event_id,)
    if request.user == event.organiser:
        if request.method == 'POST':
            form = CreateEventForm(request.POST, instance=event)
            if form.is_valid():
                form.save(commit=False)
                event.approved = False
                event.save()
                messages.add_message(request, messages.SUCCESS, 'Event has been updated and is awaiting approval.')
                return HttpResponseRedirect(reverse('user_events'))
        else:
            form = CreateEventForm(instance=event)
        return render(request, 'events/update_event.html', {'form': form})

@login_required
def attend_event(request, event_id):
    """
    allows users to record their
    intention to attend and event
    """

    event = Event.objects.get(pk=event_id)

    if event.max_attendees == 0 or event.attendees.count() < event.max_attendees:
        if request.method == 'POST':
            event.attendees.add(request.user)
            messages.add_message(request, messages.SUCCESS, "You're attending!")
            return redirect('attending_events')
    else:
        messages.warning(request, "Sorry, this run is full")
        return redirect('event_list')

@login_required
def cancel_attendance(request, event_id):
    """
    allows users to remove themselves
    from an event they have said they
    will attend
    """
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        if request.user in event.attendees.all():
            event.attendees.remove(request.user)
            messages.add_message(request, messages.SUCCESS, "You've cancelled your attendance.")
            return redirect('event_list')
    else:
        messages.add_message(request, messages.SUCCESS, "you can only remove yourself from runs")
        return render(request, 'prohibited.html')

@login_required
def user_attending_events(request):
    """
    A list of events in which the user
    has said they will be attending, split
    into past and future in the template
    """
    user = request.user
    events = Event.objects.filter(attendees=user)
    current_date = timezone.now().date()
    return render(request, 'events/attending_events.html', {'events': events, 'current_date': current_date,})