import './SectionTitle.css';

function SectionTitle({
  title = 'Section Title',
  inverse = false,
}) {
  return (
    <div className={`section-title${inverse ? ' inverse' : ''}`}>	
      <h1>{title}</h1>
    </div>
  );
}

export default SectionTitle;
