from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.forms.widgets import Widget


class LeafletMapWidget(Widget):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(
            u'<div id="map_canvas"></div><input type="hidden" value="%s" %s />'
            % (conditional_escape(force_unicode(value)),
               flatatt(final_attrs),
               ))
