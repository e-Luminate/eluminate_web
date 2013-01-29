#from django.shortcuts import get_object_or_404, redirect, render
#from events.models import Day, Event
#from django.views.decorators.http import require_http_methods
#
#def events_create(request):
#    if request.user.is_authenticated():
#        event = Event.objects.create(start_time = request.POST['start_time'], end_time = request.POST['end_time'])
#        for day in Day.objects.all():
#            if str(day.id) in request.POST:
#                event.days.add(day)
#        return redirect('/profile/events/')
#    else:
#        raise Http401
#
#def events_delete(request, event_id):
#    if request.user.is_authenticated():
#        return redirect('/profile/events/')
#    else:
#        raise Http401
#
#@require_http_methods(["GET"])
#def events_edit(request, event_id):
#    if request.user.is_authenticated():
#        # At some point we need to check that the user is allowed to edit the specific event, when the rest of the system is in place
#        return render(request, 'participant_profile/events/edit.html')
#    else:
#        return redirect('/login/')
#
#def events_index(request):
#    events = Event.objects.all()
#    return render(request, 'participant_profile/events/index.html', {'events': events})
#
#@require_http_methods(["POST"])
#def events_item_dispatch(request, event_id):
#    if request.POST['__method'] == 'put':
#        return events_update(request, event_id)
#    elif request.POST['__method'] == 'delete':
#        return events_delete(request, event_id)
#    else:
#        raise Http405
#
#@require_http_methods(["GET"])
#def events_new(request):
#    if request.user.is_authenticated():
#        return render(request, 'participant_profile/events/new.html', {'all_days': Day.objects.all})
#    else:
#        return redirect('/login')
#
#@require_http_methods(["GET", "POST"])
#def events_dispatch(request):
#    if request.method == 'GET':
#        return events_index(request)
#    else: # POST
#        return events_create(request)
#
#def events_update(request, event_id):
#    if request.user.is_authenticated():
#        # At some point we need to check that the user is allowed to update the specific event, when the rest of the system is in place
#        return redirect('profile/events')
#    else:
#        raise Http401
#    
#@require_http_methods(["GET", "POST"])
#def root_dispatch(request):
#    if request.method == 'GET':
#        return show(request)
#    else: # POST
#        if request.POST['__method'] == 'put':
#            return update(request)
#        else:
#            raise Http405
#
#def show(request):
#    return render(request, 'participant_profile/show.html')
#
#def update(request):
#    raise Http405
