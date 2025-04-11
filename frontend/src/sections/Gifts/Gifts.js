import './Gifts.css';
import SectionTitle from '../../components/sectionTitle/SectionTitle';

function Gifts() {
  return (
    <section className="gifts">
      <SectionTitle title="Regalos" inverse={true} />
      <div className="gifts-content">
        <p>
          Aunque esto sea un festival, no tienes que comprar la entrada.
        </p>
        <p>
          Si a pesar de todo quieres hacernos un regalo y prefieres 
          no llevar un sobre en el escote, este es nuestro número de cuenta:
        </p>
        <h4 className="gifts-number">
          ES00 1234 5678 9101 1121
        </h4>
      </div>
    </section>
  );
}

export default Gifts;
