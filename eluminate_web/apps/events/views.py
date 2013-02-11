from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.contrib.gis.geos import Polygon

from braces.views import LoginRequiredMixin

from maps.models import Location
from maps.utils import get_search_polygon, calculate_bounds
from participant.mixins import CategoryFilterMixin

from .models import Event
from .forms import EventForm
   
   
class EventParticipantApprovedMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        try:
            request.user.participant # Checking if the user is participant at all.
            
            if not request.user.participant.approved():
                msg = "Your Event will only be visible once you have been approved as a participant."
                messages.add_message(request, messages.INFO, msg)
                
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
    
    def render_to_response(self, context, **kwargs):
        object = self.get_object()
        if not object.participant.approved():
            # If the current user is the same that has create the event we show it
            if self.request.user == object.participant.user:    
                msg = "Your Event will only be visible once you have been approved as a participant."
                messages.add_message(self.request, messages.INFO, msg)
                context = self.get_context_data(**kwargs)
            else: # for all the other we redirect to the homepage.
                return HttpResponseRedirect(reverse_lazy('home'))
        return super(EventDetail, self).render_to_response(context, **kwargs)
    
    

class EventList(CategoryFilterMixin, ListView):
    
    model = Event
    queryset = Event.objects.filter(participant__approved_on__lt=now())

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()

        if self.selected_category_id:
            owner_in_category_query = Q(participant__categories=self.selected_category_id)
            approved_collaborators_query = ~Q(collaborators__approved_on=None)
            collaborators_in_category_query = Q(collaborators__categories=self.selected_category_id)
            queryset = queryset.filter(owner_in_category_query | approved_collaborators_query & collaborators_in_category_query).distinct()

        if self.request.GET.has_key("q"):
            queryset = queryset.filter(name__icontains=self.request.GET["q"])
        return queryset
    
    def get_template_names(self):
        template = super(EventList, self).get_template_names()
        if self.request.is_ajax():
            template = "events/_event_map_list.html"
        return template
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax(): #map has been zoomed or dragged.
            poly, map_bounds = get_search_polygon(request)
            self.object_list = self.get_queryset().filter(location__marker__within=poly)
            context = self.get_context_data(object_list=self.object_list)
            context['map_bounds'] = map_bounds
            return self.render_to_response(context, **kwargs)
        
        else: # we load the page for the first time.
            self.object_list = self.get_queryset()
            context = self.get_context_data(object_list=self.object_list)
            locations = Location.objects.filter(event__in=self.object_list)
            map_bounds = calculate_bounds(locations)
            context['map_bounds'] = map_bounds
            return self.render_to_response(context, **kwargs)

class EventListUser(EventModelOwnerRestrictedMixin, ListView):

    model = Event
    template_name = "events/event_list_user.html"
    
    
                

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
    
