from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy

from braces.views import LoginRequiredMixin

from .models import Participant
from .mixins import ParticipantMixin
from .forms import ParticipantForm


class ParticipantLandingView(ParticipantMixin, TemplateView):
    template_name = 'participant/participant_landing.html'



class ParticipantDetailView(ParticipantMixin, DetailView):
    template_name = 'participant/participant_detail.html'
    model = Participant
    context_object_name = 'current_participant'
    
    def render_to_response(self, context, **kwargs):
        participant = self.get_object()
        if not participant.approved():
            # If the current user is the same that has create the event we show it
            if self.request.user == participant.user:    
                msg = "Your Participant will be visible only when your user will be approved as participant."
                messages.add_message(self.request, messages.INFO, msg)
                context = self.get_context_data(**kwargs)
            else: # for all the other we redirect to the homepage.
                return HttpResponseRedirect(reverse_lazy('home'))
        return super(ParticipantDetailView, self).render_to_response(context, **kwargs)



class ParticipantFilterRedirectView(ParticipantMixin, RedirectView):
    url = 'X'
    query_string = True

    def get_redirect_url(self, **kwargs):
        query_string = super(ParticipantFilterRedirectView, self).get_redirect_url(**kwargs)[len(self.url):]
        participants = self.get_participant_list()
        if participants:
            return reverse('participant_detail', kwargs={'slug': participants[0].slug}) + query_string
        else:
            return reverse('participant_landing') + query_string

class ParticipantCreateView(LoginRequiredMixin, CreateView):
    model = Participant
    form_class = ParticipantForm
    
    def get(self, request, *args, **kwargs):
        try:
            request.user.participant
            return HttpResponseRedirect(reverse_lazy("participant_update", 
                                                     kwargs={"slug" : request.user.participant.slug}
                                                     )
                                        )
        except Participant.DoesNotExist:
            pass # we return the normal form
        return super (ParticipantCreateView, self).get(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ParticipantCreateView, self).form_valid(form)
        
class ParticipantUpdateView(LoginRequiredMixin, UpdateView):
    model = Participant
    form_class = ParticipantForm
    
class ParticipantDeleteView(LoginRequiredMixin, DeleteView):
    model = Participant