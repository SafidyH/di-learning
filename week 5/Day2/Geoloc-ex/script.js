function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      alert('Geolocation is not supported by your browser.');
    }
  }
  
  function showPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const output = document.getElementById('output');
    output.textContent = 'Latitude: ' + latitude + '\nLongitude: ' + longitude;
  }