from django.shortcuts import get_object_or_404, redirect, render
from events.models import Day, Event
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def index(request):
    days = map(lambda x:{'day':x, 'events':map(lambda y:{'event': y, 'participant': y.participant}, x.event_set.all())}, Day.objects.all())
    return render(request, 'events/index.html', {'days': days})

@require_http_methods(["GET"])
def show(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    days_string = str(', ').join(map(lambda x: x.name, event.days.all()))
    return render(request, 'events/show.html', {'event': event, 'participant': event.participant, 'days': days_string})
    
