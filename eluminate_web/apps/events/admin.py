from django.contrib import admin
from events.models import Event, Day

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'participant', 'priority', 'isEvent', 'featured')
    list_editable = ('priority', 'isEvent', 'featured')
    ordering = ('-featured','-isEvent','-priority')

    filter_horizontal = ('days',)

admin.site.register(Event, EventAdmin)

admin.site.register(Day)
