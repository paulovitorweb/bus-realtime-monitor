var map = L.map('map', {
    maxBounds: [[-7.040130, -34.965619], [-7.253412, -34.787168]],
    minZoom: 12,
    maxZoom: 18
}).setView([-7.145422, -34.859948], 12)

var setBaseMap = L.tileLayer(mapTileLayer, {
    attribution: mapAttribution
}).addTo(map)

function addTerminalToMap(geojson) {
    layer = L.geoJSON(geojson, {onEachFeature: onEachTerminal}).addTo(map);
}

function onEachTerminal(feature, layer) {
    if (feature.properties) {
        layer.bindPopup(feature.properties.name)
    }
}

fetch('ws/terminal/')
    .then(response => response.json())
    .then(data => addTerminalToMap(data))

var busIcon = L.icon({
    iconSize: [25, 33],
    iconAnchor: [16, 33],
    popupAnchor: [-3, -34],
    iconUrl: iconUrl
})

const busSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/map/'
)

var markers = {}
var busesInside = {}

busSocket.addEventListener('message', function(e) {
    const data = JSON.parse(e.data)
    const busId = data.bus_id
    const time = data.time
    const event = data.event

    var ul = document.getElementById('control-buses')

    if (event) {
        var li = document.createElement('li')
        li.setAttribute('class', 'fade-in')
        li.innerHTML = `<small>${time}</small> Veículo <span>${busId}</span> ${event}`
        ul.prepend(li)
    }

    if (!markers[busId]) {
        markers[busId] = L.marker([data.latitude, data.longitude], {icon: busIcon})
            .addTo(map)
            .bindPopup(`Veículo ${busId}`)
    } else {
        markers[busId].setLatLng([data.latitude, data.longitude])
    }
})

busSocket.addEventListener('close', function(e) {
    console.error('Socket closed!')
})