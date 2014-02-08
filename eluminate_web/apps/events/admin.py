from django.contrib import admin
from events.models import Event, Day

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'participant', 'priority', 'isEvent', 'featured')
    list_editable = ('priority', 'isEvent', 'featured')
    filter_horizontal = ('days',)
    ordering = ('-featured','-isEvent','-priority')
    pass

admin.site.register(Event, EventAdmin)

admin.site.register(Day)
