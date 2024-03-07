## Setup

1. **Prerequisites:**

   - Ensure you have a working GeoNode project setup.
   - MapStore is integrated within your GeoNode instance.

2. **Installation:**
   - Clone this repository into your project directory.
   - Ensure all dependencies are installed by running `pip install -r requirements.txt` for Python dependencies and `npm install` for JavaScript dependencies.

## Usage

1. **Python Setup:**

   - Integrate the `models.py` and `views.py` into your Django app. These files handle the STA data fetching from the backend.

2. **JavaScript Integration:**
   - Place `staDataFetcher.js` and `staLayerAdder.js` in the `src/utils/` directory of your frontend project.
   - Import and utilize these utilities in your MapComponent or similar component responsible for MapStore integration to fetch STA data and add it as a map layer.

## Features

- Fetches STA data through a Django backend setup.
- Visualizes STA data as a new layer in MapStore within GeoNode.
- Provides a flexible foundation for further customization and integration of additional data sources.

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, file issues, and participate in the development process.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.

## Acknowledgments

- The GeoNode team for providing an excellent platform for geospatial data sharing and management.
- The MapStore team for their versatile GIS web mapping solution.
