
from django.urls import path
from . import views

urlpatterns = [

    # Homepage
    path('', views.home, name='home'),

    # Admin Dashboard
    path('dashboard/', views.admin_dashboard, name='dashboard'),

    # All Events Management
    path(
        'dashboard/events/',
        views.manage_events,
        name='manage_events'
    ),

    # Add Event
    path('dashboard/events/add/', views.add_event, name='add_event'),

    # Edit Event
    path(
        'dashboard/events/edit/<int:event_id>/',
        views.edit_event,
        name='edit_event'
    ),

    # Delete Event
    path(
        'dashboard/events/delete/<int:event_id>/',
        views.delete_event,
        name='delete_event'
    ),

    # Users Management
    path(
        'dashboard/users/',
        views.admin_users,
        name='admin_users'
    ),
]
