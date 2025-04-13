import './Hero.css';

import { useState, useEffect } from 'react';

import mobileBanner from '../../img/mobile-banner.svg';
import desktopBanner from '../../img/desktop-banner.svg';

function Hero() { 
  const [width, setWidth] = useState(window.innerWidth);
  const [isMobile, setIsMobile] = useState(width <= 768);
  
  useEffect(() => {
    const handleResize = () => {
      setWidth(window.innerWidth);
      setIsMobile(window.innerWidth <= 768);
    };

    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const banner = isMobile ? mobileBanner : desktopBanner;

  return (
    <section className="hero">
      <div className="hero-content">
        <img src={banner} alt="Hero" className="hero-image" />
      </div>
    </section>
  );
}
  
export default Hero;
  