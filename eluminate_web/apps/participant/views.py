from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from participant.models import Category, Participant

class ParticipantMixin(object):
    def set_selected_category(self, request):
        self.selected_category_id = int(request.GET.get('category', '0'))

    def get_participant_list(self):
        participant_list = Participant.objects_approved.all()
        if self.selected_category_id: 
            participant_list = participant_list.filter(category__id=self.selected_category_id)
        return participant_list.order_by('name')

    def get_active_category_list(self):
        active_category_ids = Participant.objects_approved.distinct('category').values_list('category_id', flat=True)
        return Category.objects.filter(id__in=active_category_ids).order_by('-id')

    def get_participant_context_data(self):
        context = {}
        context['selected_category_id'] = self.selected_category_id
        context['participant_list'] = self.get_participant_list()
        context['category_list'] = self.get_active_category_list()
        return context

class ParticipantLandingView(TemplateView, ParticipantMixin):
    template_name = 'participant/participant_landing.html'

    def get(self, request, *args, **kwargs):
        self.set_selected_category(request)
        return super(ParticipantLandingView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ParticipantLandingView, self).get_context_data(**kwargs)
        context.update(self.get_participant_context_data())
        return context

class ParticipantDetailView(DetailView, ParticipantMixin):
    template_name = 'participant/participant_detail.html'
    model = Participant
    context_object_name = 'current_participant'

    def get(self, request, *args, **kwargs):
        self.set_selected_category(request)
        return super(ParticipantDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ParticipantDetailView, self).get_context_data(**kwargs)
        context.update(self.get_participant_context_data())
        return context

class ParticipantFilterRedirectView(RedirectView, ParticipantMixin):
    url = 'X'
    query_string = True

    def get(self, request, *args, **kwargs):
        self.set_selected_category(request)
        return super(ParticipantFilterRedirectView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        query_string = super(ParticipantFilterRedirectView, self).get_redirect_url(**kwargs)[len(self.url):]
        participants = self.get_participant_list()
        if participants:
            return reverse('participant_detail', kwargs={'slug': participants[0].slug}) + query_string
        else:
            return reverse('participant_landing') + query_string
