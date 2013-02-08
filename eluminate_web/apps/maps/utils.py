# Utils for maps.

from datetime import datetime
from django.contrib.gis.geos import Polygon

import pytz
utc=pytz.UTC

from models import Location

DEFAULT_POLY_COORDS = [(0.02780914306640625, 52.158980248467095), #(sw_x,sw_y)
                       (0.22350311279296875 , 52.158980248467095), #(ne_x,sw_y)
                       (0.22350311279296875 , 52.253657959623055), #(ne_x,ne_y)
                       (0.02780914306640625, 52.253657959623055), #(sw_x,ne_y)
                       (0.02780914306640625, 52.158980248467095)] #(sw_x,sw_y)

#poly_coords = [(sw_x,sw_y), (ne_x,sw_y), (ne_x,ne_y), 
#                       (sw_x,ne_y), (sw_x,sw_y)]

DEFAULT_CENTER_OBJ = {"x" : 0.12249999999994543, "y" : 52.20005469158063 }


def get_search_polygon(request):
    """Creates a polygon extracing the value from the request.
     
     Params
     ------
     request: has to have 4 GET parameter:
     sw_x, sw_y, ne_x, ne_y
     for example:
     GET /events/map?sw_y=52.19655&sw_x=0.10316&ne_y=52.21759ne_x=0.15329
     
     Return
     ------
     polygon - GEOS Polygon
     bounds - bounds used by leaflet to pan the map
     """
    
    try:
        sw_x = float(request.GET.get('sw_x'))
        sw_y = float(request.GET.get('sw_y'))
        ne_x = float(request.GET.get('ne_x'))
        ne_y = float(request.GET.get('ne_y'))
        
    except:
        msg = 'Did not get proper map boundaries'
        return HttpResponse(simplejson.dumps(dict(message=msg)))
    # polygon for the search
    poly_coords = [(sw_x,sw_y), (ne_x,sw_y), (ne_x,ne_y), 
                   (sw_x,ne_y), (sw_x,sw_y)]
    
    # We extracted them from the poly
    sw_x, sw_y = poly_coords[0][0], poly_coords[0][1]
    ne_x, ne_y = poly_coords[2][0], poly_coords[2][1]
    # Swap them to be ready for leaflet
    bounds = [[sw_y, sw_x], [ne_y, ne_x]]
    poly = Polygon(poly_coords)

    return poly, bounds

def calculate_center(locations):
    "Calculate the center of different locations"
    if locations is None:
        return DEFAULT_CENTER_OBJ
    elif len(locations) == 1:
        
        marker = locations[0].marker
        center = {"x" : marker.x, "y" : marker.y}
        return  center
    elif len(locations) > 2:
        markers_x = []
        markers_y = []
        for location in locations:
            markers_x.append(location.marker.x)
            markers_y.append(location.marker.y)
            
        center_x = _calc_middle_point(markers_x)
        center_y = _calc_middle_point(markers_y)
        center = {"x" : center_x, "y" : center_y}
        return center
    else:
        return DEFAULT_CENTER_OBJ


def _calc_middle_point(values):
    
    minimum = min(values)
    maximum = max(values)
    delta = maximum - minimum
    middle_point = minimum + delta/2
    return middle_point
        
def calculate_bounds(locations):        
 
    if locations:
        min_x, min_y, max_x, max_y = None, None, None, None
        # we search for the borders. 
        # this is quite slow, I guess we will need to 
        # find a way to speed it up
        
        for loc in locations:
            if min_x is None:
                min_x = loc.marker.x
            elif loc.marker.x < min_x :
                min_x = loc.marker.x
            if max_x is None:
                max_x = loc.marker.x
            elif loc.marker.x > max_x:
                max_x = loc.marker.x
            if min_y is None:
                min_y = loc.marker.y
            elif loc.marker.y < min_y :
                min_y = loc.marker.y
            if max_y is None:
                max_y = loc.marker.y
            elif loc.marker.y > max_y:
                max_y = loc.marker.y
            
        OFFSET = 0.01
        coords = [min_x, max_x, min_y, max_y]
    
        min_x -= OFFSET
        max_x += OFFSET
        min_y -= OFFSET
        max_y += OFFSET
        
        southWest = [min_y, min_x]
        northEast = [max_y, max_x]
        
        return [southWest, northEast]
    
        
        