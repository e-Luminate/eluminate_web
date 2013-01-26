from django.shortcuts import get_object_or_404, redirect, render
from events.models import Day, Event
from django.views.decorators.http import require_http_methods

def create(request):
    event = Event.objects.create(start_time = request.POST['start_time'], end_time = request.POST['end_time'])
    for day in Day.objects.all():
        if str(day.id) in request.POST:
            event.days.add(day)
    return redirect('/events')

def delete(request, event_id):
    return redirect('/events')

@require_http_methods(["GET"])
def edit(request, event_id):
    return render(request, 'events/edit.html')

def index(request):
    event_list = Event.objects.all
    return render(request, 'events/index.html', {'event_list': event_list})

@require_http_methods(["GET", "POST"])
def item_dispatch(request, event_id):
    if request.method == 'GET':
        return show(request, event_id)
    else: # POST, which we will interpret as a PUT or DELETE
        if request.POST['__method'] == 'put':
            return update(request, event_id)
        elif request.POST['__method'] == 'delete':
            return delete(request, event_id)
        else:
            raise Http405

@require_http_methods(["GET"])
def new(request):
    return render(request, 'events/new.html', {'all_days': Day.objects.all})

@require_http_methods(["GET", "POST"])
def root_dispatch(request):
    if request.method == 'GET':
        return index(request)
    else: # POST
        return create(request)

def show(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    days_string = str(', ').join(map(lambda x: x.name, event.days.all()))
    return render(request, 'events/show.html', {'start_time': event.start_time, 'end_time': event.end_time, 'days': days_string})

def update(request, event_id):
    return redirect('/events/%(id)d' % {'id': event_id})
