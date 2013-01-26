from django.http import HTTPResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    event_list = Event.objects
    return render(request, 'events/index.html', {'event_list': event_list})

def show(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    return render(request, 'events/index.html', {'event': event})
