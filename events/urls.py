from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('admin_approval/<int:event_id>/', views.admin_event_approval, name='admin_approval'),
    path('admin_event_approval', views.admin_event_approval_list, name='admin_event_approval'),
    path('create_event', views.create_event, name='create_event'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('user_events', views.user_events, name='user_events'),
    #path('attending_events', views.attending_events, name='attending_events'),

]