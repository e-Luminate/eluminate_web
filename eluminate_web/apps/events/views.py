from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Event
from .forms import EventForm
   

class EventDetail(DetailView):
    
    model = Event

class EventList(ListView):
    
    model = Event

        
class EventModelOwnerRestrictedMixin(object):
    model = Event
    
    def get_queryset(self):
        "Restricting to only the Events the user owns."
        
        queryset = super(EventModelOwnerRestrictedMixin, self).get_queryset()
        queryset.filter(participant__user=self.request.user)
         
        return queryset        

class EventCreate(CreateView):
    
    model = Event
    form_class = EventForm

    def form_valid(self, form):
        
        form.instance.participant = self.request.user.participant
        form.save()
        return super(EventCreate, self).form_valid(form)
        

class EventUpdate(EventModelOwnerRestrictedMixin, UpdateView):
    
    model = Event
    form_class = EventForm
    
class EventDelete(EventModelOwnerRestrictedMixin, DeleteView):
    
    model = Event
    