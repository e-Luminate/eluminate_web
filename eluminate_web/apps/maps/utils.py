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


def search_items_within_poly(poly_coords, queryset):
    """Search the items which location is contained within the poly and return 
    them as a list of queryset.
    
    Params:
    -------
    poly_coords - Must be a set of coords (long, lat) where the last one should 
                  be equal to the first point. 
                  Example: default_poly_coords = [(0.08, 52.19), (0.15, 52.19), 
                                                  (0.15, 52.21), (0.08, 52.21),
                                                  (0.08, 52.19)] 
    """
    
    poly = Polygon(poly_coords)
    items_query_set = queryset.filter(item_template__producer__user__profile__location__marker__within=poly)

                     
    return items_query_set


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
    
        
        