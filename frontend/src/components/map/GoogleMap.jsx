import { APIProvider, Map } from "@vis.gl/react-google-maps";

function GoogleMap({ center, zoom, style, children }) {
    const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;
    const mapId = import.meta.env.VITE_GOOGLE_MAPS_MAP_ID;

    return <APIProvider
        apiKey={apiKey}
    >
        <Map
            mapId={mapId}
            defaultCenter={center}
            defaultZoom={zoom}
            style={style ?? { width: '100%', height: '100%' }}
        >
            {children}
        </Map>
    </APIProvider>
}

export default GoogleMap;
