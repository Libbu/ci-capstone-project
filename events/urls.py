from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('create_event', views.create_event, name='create_event'),
    path('user_events', views.user_events, name='user_events'),
    path('update_event/<int:event_id>/update/', views.update_event, name='update_event'),  # noqa
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),  # noqa
    path('attending_events', views.user_attending_events, name='attending_events'),  # noqa
    path('attend_event/<event_id>', views.attend_event, name='attend-event'),
    path('cancel_attendance/<event_id>', views.cancel_attendance, name="cancel-attendance"),  # noqa
    path('admin_event_approval', views.admin_event_approval_list, name='admin_event_approval'),  # noqa
    path('admin_approval/<int:event_id>/', views.admin_event_approval, name='admin_approval'),  # noqa
    path('<int:event_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # noqa
    path('<int:event_id>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),  # noqa
]