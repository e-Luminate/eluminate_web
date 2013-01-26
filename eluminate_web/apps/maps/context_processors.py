# Used to query an address and return results 
from geopy import geocoders

#initializing here to have just one, and to not create one per request.
g = geocoders.OpenMapQuest()

# Located in my app that processes orders
def lookup_address(request):
    if 'address_query' in request.GET and request.GET['address_query']:
        
        lookup_address = g.geocode(request.GET['address_query'], exactly_one=False) 
        print request.GET['address_query']
        return { 'lookup_address' : lookup_address,
                'lookup_address_length' : len(lookup_address)
                }
    else: return {'lookup_address_length' : 0}