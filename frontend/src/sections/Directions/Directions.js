import './Directions.css';

import SectionTitle from '../../components/sectionTitle/SectionTitle';

function Directions () {
  const places = [
    {
        title: 'La Iglesia',
        name: 'Iglesia de Santa María de la Paz',
        address: 'Calle de la Iglesia, 123, 28001 Madrid',
    },
    {
        title: 'La Finca',
        name: 'Hacienda El Loreto',
        address: 'Calle de la Finca, 456, 28002 Madrid',
    },
  ]

  return (
    <section className="directions">
      <SectionTitle title="El sitio" />  
      <div className="directions-content">
        <div className="map">
            <img src="https://placehold.co/500?text=MAP" alt="map" />
        </div>
        <div className="directions-text">
            {places.map((place) => (
                <div className="place">
                    <h2>{place.title}</h2>
                    <h3>{place.name}</h3>
                    <p>{place.address}</p>
                </div>
            ))}
        </div>
      </div>
    </section>
  );
}

export default Directions;
