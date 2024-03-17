from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('admin_event_approval', views.admin_event_approval, name='admin_event_approval'),
    path('create_event', views.create_event, name='create_event'),
    path('event/<int:event_id/', views.event_detail, name='event_detail'),
]