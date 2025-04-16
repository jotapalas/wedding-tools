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
      subtitle: 'Ácido y alurónico',
      image: ceremony,
      altText: 'Vamos vamos, que nos casamos',
    },
    {
      time: '20:00',
      title: 'La Guagua',
      subtitle: 'Cuando zarpa el amor',
      image: bus,
      altText: 'Viva nuestro conductor, conductor, conductor',
    },
    {
      time: '20:30',
      title: 'La Verbena',
      subtitle: 'Una copita pa\' brindar y otras dos pa\' los dos que vienen conmigo',
      image: cocktail,
      altText: 'Ven a ver, hay de beber',
    },
    {
      time: '22:00',
      title: 'El Condumio',
      subtitle: 'Que me coma el tigre',
      image: dinner,
      altText: 'Dame más gasolina',
    },
    {
      time: '00:00',
      title: 'El Ballroom',
      subtitle: 'Como si fuera esta noche la última vez',
      image: party,
      altText: 'Yo quiero bailar, toda la noche',
    },
    {
      time: '05:30',
      title: 'Back to Guagua',
      subtitle: 'Quién le ha dicho a usted que quiero que conduzcan por mí',
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
            key={index}
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
