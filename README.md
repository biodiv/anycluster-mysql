anycluster (MySQL version)
============================

This is the mysql version of https://github.com/biodiv/anycluster/

It differs from the postgis version. Currently, only centroid clustering is supported and there is no support for filters yet.

anycluster provides Server-Side clustering of map markers for Geodjango. It is suitable for large amounts of markers. 
Depending on your server and personal feeling, it works very well with 200.000 to 500.000 markers.


Prequisities
============
- python 2.7 (3.x not supported)
- Django 1.6
- GeoDjango
- MySQL 5.0+
- a spatial column holding your point coordinates
- a spatial index on that column


Installation
============


1. unzip the folder anycluster into your project directory
2. add ‘anycluster’ to your INSTALLED_APPS
3. required SETTINGS (settings.py)

    ```ANYCLUSTER_GEODJANGO_MODEL = "yourapp.your_geodjango_model"```
    
    ```ANYCLUSTER_COORDINATES_COLUMN = "your_geometric_column"```

4. add the following to your STATICFILES_DIRS (settings.py)

    ``` '/PATH_TO_YOUR_PROJECT_FOLDER/anycluster/static' ```

5. urls.py

    ```url(r'anycluster/', include('anycluster.urls')),```


USAGE
=====
1.Load the required modules

```
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?&key=YOURKEY&sensor=false"></script>
<script type="text/javascript" src="{% static 'anycluster/anycluster.js' %}"></script>
<script type="text/javascript" src="{% static 'anycluster/django_ajax_csrf.js' %}"></script>
<script type="text/javascript" src="{% static 'anycluster/anycluster_marker.js' %}"></script>
<link rel="stylesheet" href="{% static 'anycluster/anycluster.css' %}">
```


2.start clustering


```javascript
var anyclusterSettings = {
				mapType : "google",
				gridSize: 64, //integer
				zoom: 3, //initial zoom
				center: [10,11], //initial center in lng lat
				MapTypeId: "TERRAIN", //ROADMAP,SATELLITE,HYBRID or TERRAIN
				clusterMethod : "centroid", //currently only centroid is supported
				iconType: "exact",
				onFinalClick : function(entries){
					//do something with the html(entries)
				}
	
}
		
window.onload = function(){
				
		anycluster = new Anycluster("div_id", anyclusterSettings);
			
}
```
