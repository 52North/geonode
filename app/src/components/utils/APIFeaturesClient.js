const baseUrl = "https://developer.ogc.org/collections/{collectionId}/items";
async function fetchData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Error fetching data: ${response.statusText}`);
  }
  return await response.json();
}

async function getCollections() {
  const url = `${baseUrl}/collections`;
  const data = await fetchData(url);
  console.log("Collections:", data);
  return data;
}

async function getCollectionInfo(collectionId) {
  const url = `${baseUrl}/collections/${collectionId}`;
  const data = await fetchData(url);
  console.log("Collection Info:", data);
  return data;
}

async function getCollectionData(collectionId) {
  const url = `${baseUrl}/collections/${collectionId}/items`;
  const data = await fetchData(url);
  console.log("Collection Data:", data);
  return data;
}

// A simple example usage of the follwoing functions
getCollections()
  .then((collections) => {
    if (collections.length > 0) {
      const firstCollectionId = collections[0].id;
      getCollectionInfo(firstCollectionId)
        .then(() => getCollectionData(firstCollectionId))
        .catch((error) => console.error("Error:", error));
    } else {
      console.log("No collections found.");
    }
  })
  .catch((error) => console.error("Error:", error));
