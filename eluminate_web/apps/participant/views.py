from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from participant.models import Category, Participant

class ParticipantLandingView(TemplateView):
    template_name = 'participant/participant_landing.html'

    def get_context_data(self, **kwargs):
        context = super(ParticipantLandingView, self).get_context_data(**kwargs)
        context['participant_list'] = Participant.objects.all().order_by('name')
        context['category_list'] = Category.objects.all()
        return context

class ParticipantDetailView(DetailView):
    template_name = 'participant/participant_detail.html'
    model = Participant

    def get_context_data(self, **kwargs):
        context = super(ParticipantDetailView, self).get_context_data(**kwargs)
        context['participant_list'] = Participant.objects.all().order_by('name')
        context['category_list'] = Category.objects.all()
        return context

