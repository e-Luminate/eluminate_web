from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from participant.models import Category, Participant

class ParticipantLandingView(TemplateView):
    template_name = 'participant/participant_landing.html'

    def get(self, request, *args, **kwargs):
        self.selected_category_id = int(request.GET.get('category', '0'))
        return super(ParticipantLandingView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ParticipantLandingView, self).get_context_data(**kwargs)
        context['selected_category_id'] = self.selected_category_id
        participant_list = Participant.objects.all()
        if self.selected_category_id: 
            participant_list = participant_list.filter(category__id=self.selected_category_id)
        context['participant_list'] = participant_list.order_by('name')
        used_category_ids = Participant.objects.distinct('category').values_list('category_id', flat=True)
        context['category_list'] = Category.objects.filter(id__in=used_category_ids).order_by('-id')
        return context

class ParticipantDetailView(DetailView):
    template_name = 'participant/participant_detail.html'
    model = Participant
    context_object_name = 'current_participant'

    def get(self, request, *args, **kwargs):
        self.selected_category_id = int(request.GET.get('category', '0'))
        return super(ParticipantDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ParticipantDetailView, self).get_context_data(**kwargs)
        context['selected_category_id'] = self.selected_category_id
        participant_list = Participant.objects.all()
        if self.selected_category_id: 
            participant_list = participant_list.filter(category__id=self.selected_category_id)
        context['participant_list'] = participant_list.order_by('name')
        used_category_ids = Participant.objects.distinct('category').values_list('category_id', flat=True)
        context['category_list'] = Category.objects.filter(id__in=used_category_ids).order_by('-id')
        return context

