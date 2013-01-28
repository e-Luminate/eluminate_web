from django.views.generic.base import TemplateView

from participant.models import Category, Participant

class ParticipantBaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ParticipantBaseView, self).get_context_data(**kwargs)
        context['participant_list'] = Participant.objects.all().order_by('name')
        context['category_list'] = Category.objects.all()
        return context

class ParticipantLandingView(ParticipantBaseView):
    template_name = 'participant/participant_landing.html'

