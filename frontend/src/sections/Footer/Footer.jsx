import './Footer.css';

import spotifyLogo from '../../img/spotify-logo.png';
import SectionTitle from '../../components/sectionTitle/SectionTitle';

function Footer() {
  const spotifyUrl = import.meta.env.VITE_SPOTIFY_PLAYLIST_URL;

  return <section className="footer">
    <div className="footer-container">
      <p>
        Mientras se acerca el día, echa un vistazo a <span className="bold">la playlist</span>&nbsp;
        que estáis haciendo entre todos y ve ensayando los pasos prohibidos.&nbsp;
        <span className="bold">¡Nos vemos en Sevilla!</span>
      </p>
      <button
        className="spotify-playlist-button"
        onClick={() => window.open(spotifyUrl, '_blank')}
      >
        <img className="spotify-logo" src={spotifyLogo} alt="Spotify Logo" />
        <span>Escuchar Playlist</span>
      </button>
    </div>
  </section>;
}

export default Footer;
