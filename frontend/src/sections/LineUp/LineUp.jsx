import './LineUp.css';

import SectionTitle from '../../components/sectionTitle/SectionTitle';
import LineUpElement from '../../components/lineUpElement/LineUpElement';

import ceremony from '../../img/lineup/ceremony.jpg';
import bus from '../../img/lineup/bus.jpg';
import cocktail from '../../img/lineup/cocktail.jpg';
import dinner from '../../img/lineup/dinner.jpg';
import party from '../../img/lineup/party.jpg';
import endgame from '../../img/lineup/endgame.jpg';

function LineUp() {
  const lineupData = [
    {
      time: '18:30',
      title: 'El Casamiento',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: ceremony,
      altText: 'Vamos vamos, que nos casamos',
    },
    {
      time: '20:00',
      title: 'La Guagua',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: bus,
      altText: 'Viva nuestro conductor, conductor, conductor',
    },
    {
      time: '20:30',
      title: 'La Verbena',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: cocktail,
      altText: 'Ven a ver, hay de beber',
    },
    {
      time: '22:00',
      title: 'Las Viandas',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: dinner,
      altText: 'Dame más gasolina',
    },
    {
      time: '00:00',
      title: 'El Ballroom',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: party,
      altText: 'Yo quiero bailar, toda la noche',
    },
    {
      time: '05:30',
      title: 'Back to Guagua',
      subtitle: 'Lorem ipsum dolor sit amet',
      image: endgame,
      altText: 'Buenas noches, hasta mañana',
    },
  ];
  
  return (
    <section className="lineup">
      <SectionTitle title="Line Up" />
      <div className="lineup-content">
        {lineupData.map((item, index) => (
          <LineUpElement
            time={item.time}
            title={item.title}
            subtitle={item.subtitle}
            image={item.image}
            altText={item.altText}
            flexReverse={index % 2 === 1}
          />
        ))}
      </div>
    </section>
  );
}

export default LineUp;
