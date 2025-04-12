import { AdvancedMarker, Pin } from "@vis.gl/react-google-maps";

function MapPin({ title, location, style, onClick }) {
  return (
    <AdvancedMarker
      position={location}
      title={title}
      onClick={onClick}
    >
      <Pin {...style} />
    </AdvancedMarker>
  );
}

export default MapPin;
