import './Claim.css';
import claim from '../../img/claim.jpg';

function Claim() {
  return (
    <section className="claim">
      <div className="claim-content">
        <div className="claim-element claim-text">
          <p>
            Si has aguantado todos estos años de relación,<br />
            te mereces una buena fiesta.<br />
          </p>
        </div>
        <div className="claim-element claim-image">
          <img src={claim} alt="Mirando a nuestro esperanzador futuro" />
        </div>
      </div>
    </section>
  );
}

export default Claim;
