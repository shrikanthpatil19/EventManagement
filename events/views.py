
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model

from .models import Event
from .forms import EventForm


# Homepage
def home(request):
    events = Event.objects.all().order_by('date')

    return render(request, 'events/home.html', {
        'events': events
    })


# Admin Dashboard
@staff_member_required
def admin_dashboard(request):
    User = get_user_model()

    context = {
        'total_events': Event.objects.count(),
        'total_users': User.objects.count(),
        'recent_events': Event.objects.all().order_by('-id')[:5],
    }

    return render(request, 'events/dashboard.html', context)


# Add Event with Image Upload
@staff_member_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm()

    return render(request, 'events/add_event.html', {
        'form': form
    })


# Edit Event with Image Upload
@staff_member_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(
            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {
        'form': form,
        'event': event
    })


# Delete Event
@staff_member_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')

    return render(request, 'events/delete_event.html', {
        'event': event
    })


# Custom Users Management
@staff_member_required
def admin_users(request):
    User = get_user_model()

    users = User.objects.all().order_by('username')

    return render(request, 'events/users.html', {
        'users': users
    })


# Full Events Management
@staff_member_required
def manage_events(request):
    events = Event.objects.all().order_by('-date')

    return render(request, 'events/manage_events.html', {
        'events': events
    })
