from participant.models import Category, Participant

class CategoryFilterMixin(object):
    model = Category
    
    def set_selected_category(self, request):
        self.selected_category_id = int(request.GET.get('category', '0'))

    def get_active_category_list(self):
        active_category_ids = Participant.objects_approved.distinct('categories').values_list('categories', flat=True)
        return Category.objects.filter(id__in=active_category_ids).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoryFilterMixin, self).get_context_data(**kwargs)
        context['selected_category_id'] = self.selected_category_id
        context['category_list'] = self.get_active_category_list()
        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.set_selected_category(request)
        return super(CategoryFilterMixin, self).dispatch(request, *args, **kwargs)

class ParticipantMixin(CategoryFilterMixin):

    def get_participant_list(self):
        participant_list = Participant.objects_approved.all()
        if self.selected_category_id: 
            participant_list = participant_list.filter(categories=self.selected_category_id)
        return participant_list.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ParticipantMixin, self).get_context_data(**kwargs)
        context['participant_list'] = self.get_participant_list()
        return context
