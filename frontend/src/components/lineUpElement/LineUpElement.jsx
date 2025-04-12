import './LineUpElement.css';

function LineUpElement({ 
  time = '00:00',
  title = 'Line Up Element',
  subtitle = 'Subtitle',
  image = 'https://placehold.co/500?text=Image+Placeholder',
  altText = '',
  flexReverse = false,
 }) {
  return (
    <div className={
      "lineup-element"
      + (flexReverse ? " flex-reverse" : "")
    }>
      <div className="lineup-image">
        <img src={image} alt={altText} />
      </div>
      <div className="lineup-text">
        <h4>{time}</h4>
        <h3>{title}</h3>
        <p>{subtitle}</p>
      </div>
    </div>
  );
}

export default LineUpElement;
