from django.shortcuts import get_object_or_404, redirect, render
from events.models import Day, Event
from django.views.decorators.http import require_http_methods

def create(request):
    if request.user.is_authenticated():
        event = Event.objects.create(start_time = request.POST['start_time'], end_time = request.POST['end_time'])
        for day in Day.objects.all():
            if str(day.id) in request.POST:
                event.days.add(day)
        return redirect('/events/')
    else:
        raise Http401

def delete(request, event_id):
    if request.user.is_authenticated():
        return redirect('/events/')
    else:
        raise Http401

@require_http_methods(["GET"])
def edit(request, event_id):
    if request.user.is_authenticated():
        # At some point we need to check that the user is allowed to edit the specific event, when the rest of the system is in place
        return render(request, 'events/edit.html')
    else:
        return redirect('/login/')

def index(request):
    days = map(lambda x:{'day':x, 'events':map(lambda y:{'event': y, 'participant': y.participant}, x.event_set.all())}, Day.objects.all())
    return render(request, 'events/index.html', {'days': days})

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
    if request.user.is_authenticated():
        return render(request, 'events/new.html', {'all_days': Day.objects.all})
    else:
        return redirect('/login')

@require_http_methods(["GET", "POST"])
def root_dispatch(request):
    if request.method == 'GET':
        return index(request)
    else: # POST
        return create(request)

def show(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    days_string = str(', ').join(map(lambda x: x.name, event.days.all()))
    return render(request, 'events/show.html', {'event': event, 'participant': event.participant, 'days': days_string})

def update(request, event_id):
    if request.user.is_authenticated():
        # At some point we need to check that the user is allowed to update the specific event, when the rest of the system is in place
        return redirect('/events/%(id)d' % {'id': event_id})
    else:
        raise Http401
    
