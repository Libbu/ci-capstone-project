from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Event


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
