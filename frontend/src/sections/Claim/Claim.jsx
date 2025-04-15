import './Claim.css';
import claim from '../../img/claim.jpg';

function Claim() {
  return (
    <section className="claim">
      <div className="claim-content">
        <div className="claim-element claim-text">
          <p className="claim-text-title">
            Lo de la boda
          </p>
          <p className="claim-text-title">
            iba en serio
          </p>
        </div>
        <div className="claim-element claim-image">
          <img src={claim} alt="¿Ese es Mickey Mouse en patinete?" />
        </div>
      </div>
    </section>
  );
}

export default Claim;
