from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from maps.models import Location
from participant.mixins import CategoryFilterMixin

from .models import Event
from .forms import EventForm
   

class EventDetail(DetailView):
    
    model = Event

class EventList(ListView, CategoryFilterMixin):
    
    model = Event

    def get(self, request, *args, **kwargs):
        self.set_selected_category(request)
        return super(EventList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()
        if self.selected_category_id:
            queryset = queryset.filter(
                            participant__category__id=self.selected_category_id
                            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context.update(self.get_category_context_data())
        return context 

class EventListUser(LoginRequiredMixin, EventList):
    model = Event
    template_name = "events/event_list_user.html"
    
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.participant
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse_lazy('home'))
        return super(EventListUser, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super(EventListUser, self).get_queryset().filter(
                                participant=self.request.user.participant
                                )
        return queryset
        
class EventModelOwnerRestrictedMixin(object):
    model = Event
    
    def get_queryset(self):
        "Restricting to only the Events the user owns."
        
        queryset = super(EventModelOwnerRestrictedMixin, self).get_queryset().filter(
                                    participant=self.request.user.participant
                                    )
        return queryset        

class EventCreate(LoginRequiredMixin, CreateView):
    
    model = Event
    form_class = EventForm

    def get_initial(self):
        initial = super(EventCreate, self).get_initial()
        initial['location'] = Location.objects.filter(user=self.request.user)
        return initial

    def form_valid(self, form):
        
        form.instance.participant = self.request.user.participant
        form.save()
        return super(EventCreate, self).form_valid(form)
        

class EventUpdate(LoginRequiredMixin, EventModelOwnerRestrictedMixin, UpdateView):
        
    model = Event
    form_class = EventForm
    template_name = "events/event_form_update.html"
       
    def get_initial(self):
        initial = super(EventUpdate, self).get_initial()
        initial['location'] = Location.objects.filter(user=self.request.user)
        return initial
    
class EventDelete(LoginRequiredMixin, EventModelOwnerRestrictedMixin, DeleteView):
    
    model = Event
    
