from django.template import RequestContext, Context
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geos import Point
from django.contrib import messages
from utils import calculate_center, DEFAULT_CENTER_OBJ, calculate_bounds
from forms import AddLocationForm, EditLocationForm
from models import Location



import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def list(request, template='maps/locations.html'):
    
    data = {}
    locations_obj = request.user.location_set.all()
    
    data['locations'] = locations_obj
    data['username'] = request.user.username
    if locations_obj:
        data['map_bounds'] = calculate_bounds(locations_obj)
    
    return render_to_response(template,
                  data,
                  context_instance=RequestContext(request)
                  )

@csrf_protect
@login_required    
def add(request, form_class=AddLocationForm, template='maps/add_location.html'):
    center_obj = DEFAULT_CENTER_OBJ
    if request.method == 'POST': # If the form has been submitted...
        form = form_class(request.user, request.POST)
        if form.is_valid():
            
            location = form.save(commit=False)
            location.user = request.user
            location.save()
            msg = _("%(name)s has been saved.") %{'name': location.name}
            messages.add_message(request, messages.SUCCESS, msg)  
            return HttpResponseRedirect(reverse('locations_list'))
        else:
            # We re-pass the default location if the form is not valid
            location = Location()
            location.marker = Point(DEFAULT_CENTER_OBJ['x'], DEFAULT_CENTER_OBJ['y'])
        
    else:
        # A dynamically loaded form
        location = Location()
        location.marker = Point(DEFAULT_CENTER_OBJ['x'], DEFAULT_CENTER_OBJ['y'])
        form = form_class(initial={'user' : request.user,
                                   'marker' : location.marker})
        
    return render_to_response(template,
                              { "form": form, 
                                "location": location,
                               },
                              context_instance=RequestContext(request))

@csrf_protect
@login_required    
def edit(request, location_pk, form_class=EditLocationForm, template='maps/add_location.html'):
    
    location = get_object_or_404(Location, pk=location_pk)
    
    if location.user != request.user:    
        return HttpResponseRedirect(reverse('home'))
        
    if request.method == 'POST': # If the form has been submitted...    
        form = form_class(request.user, request.POST, instance=location)
        
        if form.is_valid():

            location = form.save(commit=False)
            location.save()
            msg = _("%(name)s has been saved.") %{'name': location.name}
            messages.add_message(request, messages.SUCCESS, msg)
            
            return HttpResponseRedirect(reverse('locations_list'))
        
        
    else:
        # A dynamically loaded form
        form = form_class(instance=location)
    return render_to_response(template,
                              { "form": form,
                                "location": location,
                                },
                              context_instance=RequestContext(request))
        
@csrf_protect
@login_required
def delete(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    location.delete()
    return HttpResponseRedirect(reverse('locations_list'))
