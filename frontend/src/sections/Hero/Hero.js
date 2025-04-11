import './Hero.css';
import banner from '../../img/hero-banner.jpg';

function Hero() {
    return (
      <section className="hero">
        <div className="hero-content">
          <img src={banner} alt="Hero" className="hero-image" />
        </div>
      </section>
    );
  }
  
  export default Hero;
  