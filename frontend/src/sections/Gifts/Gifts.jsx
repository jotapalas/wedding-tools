import './Gifts.css';
import SectionTitle from '../../components/sectionTitle/SectionTitle';

function Gifts() {                           
  const iban = (import.meta.env.VITE_IBAN || 'ES1234567890123456789012').replace(/\s/g,'').match(/.{1,4}/g).join(' ');
  const accountHolder = import.meta.env.VITE_ACCOUNT_HOLDER;


  return (
    <section className="gifts">
      <SectionTitle title="Regalos" inverse={true} />
      <div className="gifts-content">
        <p>
          Aunque esto sea un festival, <span className="bold">no tienes que comprar entrada.</span>
        </p>
        <p>
          Si a pesar de todo quieres hacernos un regalo y prefieres 
          no llevar <span className="bold">un sobre en el escote,</span> este es nuestro número de cuenta:
        </p>
        <div className="gifts-iban-container">
          <h4 className="gifts-iban">
            { iban }
          </h4>
          { accountHolder &&
            <h3 className="gifts-account-holder">
              { accountHolder }
            </h3>
          }
        </div>
      </div>
    </section>
  );
}

export default Gifts;
