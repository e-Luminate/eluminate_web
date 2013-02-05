
SSOUK.namespace('SSOUK.map_handler');

SSOUK.map_handler = function() {
    
    init = function() {
        var y =  52.20005469158063,
            x = 0.12249999999994543,
            zoom = 12;
        //var markersCluster = new L.MarkerClusterGroup(); // to use the markers plugin
        var markers = {};
            
        var map = new L.Map('map_canvas');
        var mapquestUrl = 'http://{s}.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png',
        	subDomains = ['otile1','otile2','otile3','otile4'],
        	mapquestAttrib = 'Data, imagery and map information provided by <a href="http://open.mapquest.co.uk" \ target="_blank">MapQuest</a>, <a href="http://www.openstreetmap.org/" target="_blank">OpenStreetMap</a> and contributors.';
                
        var mapquest = new L.TileLayer(mapquestUrl, {maxZoom: 18, attribution: mapquestAttrib, subdomains: subDomains});
        
        map.addLayer(mapquest).setView(new L.LatLng(y, x), zoom);
        
        // events 
        map.on('dragend', SSOUK.map_handler.updateDisplay);
        map.on('zoomend', SSOUK.map_handler.updateDisplay);
        
        
        //Adding our vars to Namespace
        SSOUK.map_handler.map = map;
        SSOUK.map_handler.markers = markers;
        //SSOUK.map_handler.markersCluster = markersCluster;
   }
   
    updateMarker = function(lat, lng, popup_text, location_id) {
        
        if  (! SSOUK.map_handler.markers.hasOwnProperty(location_id)) {
        	// if marker not in the map we add it
        	var marker_id = "location_" + location_id;
	        var marker = new L.Marker(new L.LatLng(lat, lng), options={"id" : marker_id});
	        
	        marker.bindPopup(popup_text);
	        //markersCluster = SSOUK.map_handler.markersCluster;
	        
	        // adding the data
	        marker['data'] = {
	        	'location_id' : location_id,
	        	'popup_text' : popup_text,
	        };
			
	        map = SSOUK.map_handler.map;
	        marker.addTo(map);
	        //map.addLayer(markersCluster);
	        SSOUK.map_handler.markers[location_id] = marker; 
	        marker.on('click', SSOUK.map_handler.onMarkerClick);       	
        }
        else {
        	// nothing for now.
        }
    }

   updateDisplay =  function(e) {
        
        var bounds = SSOUK.map_handler.map.getBounds();
        var sw = bounds.getSouthWest();
        var ne = bounds.getNorthEast();
        //console.log("sw lat "+ sw.lat + " sw lng " + sw.lng + " ne lat " + ne.lat + " ne lng " + ne.lng );
        // get the items from django
        // and update the items 
        $.get("/inventory/get_items_within_map", {
            'sw_y' : sw.lat,
            'sw_x' : sw.lng,
            'ne_y' : ne.lat,
            'ne_x' : ne.lng
        }, function (html_response) {
            $('#inventory-list').replaceWith(html_response);
        });
   }
   
  onInventoryListClick = function(event) {
  		event.preventDefault();
  		var marker = SSOUK.map_handler.markers[event.data.item_location_id];
  		var map = SSOUK.map_handler.map;
  		map.panTo(marker.getLatLng());
  		marker.openPopup();
  		var location_class_id = ".location_id_" + event.data.item_location_id;
  		SSOUK.map_handler.selectItemRow(location_class_id);
  }
  
  selectItemRow = function (location_class_id){
  		// remove old selection
  		$(".selected").removeClass("selected alert alert-info");
  		// add new
  		$(location_class_id).addClass("selected alert alert-info");
  }
   
  onMarkerClick = function(event) {
  		var location_class_id = ".location_id_" + event.target.data.location_id;
		SSOUK.map_handler.selectItemRow(location_class_id);
  }
  
  searchMarker = function(latitude, longitude, locationAddress) {
  		var map = SSOUK.map_handler.map;
  		var redMarker = L.icon({
    		iconUrl: '/site_media/static/img/marker-icon-red.png',
    		//shadowUrl: 'leaf-shadow.png',
			iconSize:     [25, 41], // size of the icon
    		//shadowSize:   [50, 64], // size of the shadow
    		iconAnchor:   [12, 41], // point of the icon which will correspond to marker's location
    		//shadowAnchor: [4, 62],  // the same for the shadow
    		popupAnchor:  [1, -34], // point from which the popup should open relative to the iconAnchor
    		
		});
		map.panTo([latitude, longitude]);
		L.marker([latitude, longitude], {icon: redMarker})
				.addTo(map).bindPopup(locationAddress);
		
  }
  
   return {
        init : init,
        updateDisplay : updateDisplay,
        updateMarker : updateMarker, 
        onMarkerClick : onMarkerClick,
        onInventoryListClick : onInventoryListClick, 
        selectItemRow : selectItemRow,
        searchMarker : searchMarker
   }
}();
 