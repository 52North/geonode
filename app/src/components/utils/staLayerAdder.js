import { Vector as VectorLayer } from 'ol/layer';
import { Vector as VectorSource } from 'ol/source';
import { GeoJSON } from 'ol/format';

async function addSTALayerToMap(map) {
    // Fetch the STA data
    const staData = await fetchSTAData();
    
    // Create a new vector source and layer using the fetched GeoJSON data
    const vectorSource = new VectorSource({
        features: new GeoJSON().readFeatures(staData),
    });

    const vectorLayer = new VectorLayer({
        source: vectorSource,
    });

    // Add the layer to the map
    map.addLayer(vectorLayer);
}
