

      /*  // Initialize the map
        function initMap() 
	{
            // Create a new map instance
            map = new google.maps.Map(document.getElementById('map-container'), {
                center: { lat: 39.951700, lng: 27.676 }, // Initial center at UPENN
                zoom: 12 // Adjust the initial zoom level as needed
            });

            // Create a marker for the selected location
            var marker = new google.maps.Marker({
                map: map,
                draggable: true,
				position: { lat: 39.951700, lng: 27.676 }// Allow the marker to be moved
            });

            // Event listener for when the marker is dragged
            marker.addListener('dragend', function () {
                // Update the manual location input with the marker's coordinates
                var position = marker.getPosition();
                document.getElementById('manual-location-input').value = position.lat() + ', ' + position.lng();
            });

            // Event listener for the manual location button
            document.getElementById('color').addEventListener('click', function () {
                var input = document.getElementById('manual-location-input').value; //required latitues and longitudes
                var coordinates = input.split(',');
                if (coordinates.length === 2) {
                    var latitude = parseFloat(coordinates[0]);
                    var longitude = parseFloat(coordinates[1]);

                    if (!isNaN(latitude) && !isNaN(longitude)) {
                        // Set the marker position and map center based on the manual input
                        var location = new google.maps.LatLng(latitude, longitude);
                        marker.setPosition(location);
                        map.setCenter(location);
                        })
                        .catch(error => console.error(error));
                    } else {
                        alert('Invalid coordinates. Please enter latitude and longitude.');
                    }
                } else {
                    alert('Invalid input. Please enter coordinates in the format: latitude, longitude.');
                }

            });
        }*/var map;

// Initialize the map
function initMap() {
    // Create a new map instance
    map = new google.maps.Map(document.getElementById('map-container'), {
        center: { lat: 39.951700, lng: 27.676 }, // Initial center at UPENN
        zoom: 12 // Adjust the initial zoom level as needed
    });

    // Create a marker for the selected location
    var marker = new google.maps.Marker({
        map: map,
        draggable: true,
        position: { lat: 39.951700, lng: 27.676 } // Allow the marker to be moved
    });

    // Event listener for when the marker is dragged
    marker.addListener('dragend', function () {
        // Update the manual location input with the marker's coordinates
        var position = marker.getPosition();
        document.getElementById('manual-location-input').value = position.lat() + ', ' + position.lng();
    });

    // Event listener for the manual location button
    document.getElementById('color').addEventListener('click', function () {
        var input = document.getElementById('manual-location-input').value; // Required latitudes and longitudes
        var coordinates = input.split(',');
        if (coordinates.length === 2) 
		{
            var latitude = parseFloat(coordinates[0]);
            var longitude = parseFloat(coordinates[1]);

            if (!isNaN(latitude) && !isNaN(longitude)) 
			{
                // Set the marker position and map center based on the manual input
                var location = new google.maps.LatLng(latitude, longitude);
                marker.setPosition(location);
                map.setCenter(location);
            } 
			else 
			{
                alert('Invalid coordinates. Please enter latitude and longitude.');
            }
        } 
		else 
		{
            alert('Invalid input. Please enter coordinates in the format: latitude, longitude.');
        }
    });
}