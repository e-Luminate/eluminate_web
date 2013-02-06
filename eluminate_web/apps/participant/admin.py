from datetime import datetime

from django.contrib import admin

from participant.models import Category, Participant

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class ApprovedListFilter(admin.SimpleListFilter):
    title = u'Approved'
    parameter_name = u'approved'
    def lookups(self, request, modeladmin):
        return (('yes', u'Yes'), ('notyet', u'Not Yet'))
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(approved_on__isnull=False)
        elif self.value() == 'notyet':
            return queryset.filter(approved_on__isnull=True)
        else:
            return queryset

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'created', 'approved', 'website')
    list_filter = (ApprovedListFilter, 'categories')
    search_fields = ('name',)
    actions = ['bulk_approve']
    date_hierarchy = 'created'

    prepopulated_fields = {'slug': ('name',)}
    #readonly_fields = ('approved_on',)

    def bulk_approve(self, request, queryset):
        objects_updated = queryset.update(approved_on=datetime.now())
        if objects_updated == 1:
            message = u'One Participant was '
        else:
            message = u'%s Participants were ' % objects_updated
        self.message_user(request, u'%s successfully approved' % message)
    bulk_approve.short_description = u'Approve the selected Participants'

admin.site.register(Participant, ParticipantAdmin)
