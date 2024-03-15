from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('<int:event_id/', views.event_detail, name='event_detail')
]