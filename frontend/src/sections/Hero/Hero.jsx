import './Hero.css';

import { useState, useEffect } from 'react';

import mobileBanner from '../../img/banner-mobile.png';
import desktopBanner from '../../img/banner-desktop.png';

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

  let banner = desktopBanner;
  if (isMobile) {
    banner = mobileBanner;
  }

  return (
    <section className="hero">
      <div className="hero-content">
        <img src={banner} alt="Hero" className="hero-image" />
      </div>
    </section>
  );
}
  
export default Hero;
  