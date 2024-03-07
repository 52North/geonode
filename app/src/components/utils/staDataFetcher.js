async function fetchSTAData() {
    const response = await fetch('/api/sta-data/');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json(); // Assuming the data is returned as GeoJSON
}
