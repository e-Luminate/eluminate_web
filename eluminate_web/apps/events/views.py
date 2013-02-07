from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from maps.models import Location
from participant.mixins import CategoryFilterMixin

from .models import Event
from .forms import EventForm
   
   
class EventParticipantApprovedMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.participant # Checking if the user is participant at all.
            
            if not request.user.participant.approved():
                messages.add_message(request, messages.WARNING, "You Entry has not yet been approved.")
                return HttpResponseRedirect(reverse_lazy('home'))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('home'))

        return super(EventParticipantApprovedMixin, self).dispatch(request, *args, **kwargs)
        
        
class EventModelOwnerRestrictedMixin(object):
    model = Event
    
    def get_queryset(self):
        "Restricting to only the Events the user owns."
        
        queryset = super(EventModelOwnerRestrictedMixin, self).get_queryset().filter(
                                    participant=self.request.user.participant
                                    )
        return queryset
   

class EventDetail(DetailView):
    
    model = Event

class EventList(CategoryFilterMixin, ListView):
    
    model = Event

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()
        if self.selected_category_id:
            queryset = queryset.filter(participant__category=self.selected_category_id
                            )
        if self.request.GET.has_key("q"):
            queryset = queryset.filter(name__icontains=self.request.GET["q"])
        return queryset
    
class EventLocationList(CategoryFilterMixin, ListView):
    
    model = Location
    template_name="events/event_map.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(EventLocationList, self).get_context_data(**kwargs)
        
        if self.request.GET.has_key("q"):
            context ['searched_events'] = Event.objects.filter(name__icontains=self.request.GET["q"])
        
        return context
    
    def get_queryset(self):
        queryset = super(EventLocationList, self).get_queryset()
        if self.selected_category_id:
            queryset = queryset.filter(event__participant__category=self.selected_category_id
                            )
        if self.request.GET.has_key("q"):
            queryset = queryset.filter(event__name__icontains=self.request.GET["q"])

        return queryset
    

class EventListUser(EventParticipantApprovedMixin, EventList):

    model = Event
    template_name = "events/event_list_user.html"
    
    def get_queryset(self):
        queryset = super(EventListUser, self).get_queryset().filter(
                                participant=self.request.user.participant
                                )
        return queryset
                

class EventCreate(EventParticipantApprovedMixin, CreateView):
    
    model = Event
    form_class = EventForm

    def get_form(self, form_class):
        form = super(EventCreate, self).get_form(form_class)
        form.fields['location'].queryset = Location.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        
        form.instance.participant = self.request.user.participant
        form.save()
        return super(EventCreate, self).form_valid(form)
        

class EventUpdate(EventParticipantApprovedMixin, EventModelOwnerRestrictedMixin, UpdateView):
        
    model = Event
    form_class = EventForm
    template_name = "events/event_form_update.html"
       
    def get_form(self, form_class):
        form = super(EventUpdate, self).get_form(form_class)
        form.fields['location'].queryset = Location.objects.filter(user=self.request.user)
        return form
    
class EventDelete(EventParticipantApprovedMixin, EventModelOwnerRestrictedMixin, DeleteView):
    
    model = Event
    
