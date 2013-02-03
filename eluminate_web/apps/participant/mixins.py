from participant.models import Category, Participant

class CategoryFilterMixin(object):
    def set_selected_category(self, request):
        self.selected_category_id = int(request.GET.get('category', '0'))

    def get_active_category_list(self):
        active_category_ids = Participant.objects_approved.distinct('category').values_list('category_id', flat=True)
        return Category.objects.filter(id__in=active_category_ids).order_by('-id')

    def get_category_context_data(self):
        context = {}
        context['selected_category_id'] = self.selected_category_id
        context['category_list'] = self.get_active_category_list()
        return context

class ParticipantMixin(CategoryFilterMixin):

    def get_participant_list(self):
        participant_list = Participant.objects_approved.all()
        if self.selected_category_id: 
            participant_list = participant_list.filter(category__id=self.selected_category_id)
        return participant_list.order_by('name')

    def get_participant_context_data(self):
        context = self.get_category_context_data()
        context['participant_list'] = self.get_participant_list()
        return context
