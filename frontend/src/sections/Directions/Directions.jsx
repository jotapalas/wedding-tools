import './Directions.css';

import SectionTitle from '../../components/sectionTitle/SectionTitle';
import GoogleMap from '../../components/map/GoogleMap';
import MapPin from '../../components/mapPin/MapPin';

function Directions () {
  const places = [
    {
        title: 'La Iglesia',
        name: 'Iglesia de Santa María de la Paz',
        address1: 'C. Bustos Tavera, 15, Casco Antiguo',
        address2: '41003 Sevilla'
    },
    {
        title: 'La Finca',
        name: 'Hacienda El Loreto',
        address1: 'Ramal, Ctra. Umbrete, 510',
        address2: ' 41807 Espartinas, Sevilla'
    },
  ]

  const locations = [
    {
      key: 'La Iglesia',
      location: { lat: 37.39470541358912, lng: -5.987896266843879 }
    },
    {
      key: 'La Finca',
      location: { lat: 37.37888530874971, lng: -6.152919431910154 }
    },
  ];

  return (
    <section className="directions">
      <SectionTitle title="El sitio" />  
      <div className="directions-content">
        <div className="map">
            <GoogleMap
              center={{ lat: 37.38851108574791, lng: -6.063924773379533 }}
              zoom={10}
              style={{ width: '100%', height: '100%' }}
            >
              {locations.map((place, index) => (
                <MapPin
                  key={index}
                  title={place.key}
                  location={place.location}
                  onClick={() => console.log(`Clicked on ${place.key}`)}
                />
              ))}
            </GoogleMap>
        </div>
        <div className="directions-text">
            {places.map((place, index) => (
                <div key={index} className="place">
                    <h2>{place.title}</h2>
                    <h3>{place.name}</h3>
                    <p>{place.address1}</p>
                    <p>{place.address2}</p>
                </div>
            ))}
        </div>
      </div>
    </section>
  );
}

export default Directions;
