import './FAQItem.css';

import moodboard from '../../img/moodboard.png';

import { useState } from 'react';
import AccommodationInfo from '../accommodationInfo/AccommodationInfo';

function FAQItem({ question, answer, includeMoodboard, includeAccommodation }) {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAnswer = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="faq-item" onClick={toggleAnswer}>
      <div
        className="faq-question"
      >
        <h4>{question}</h4>
        <span className="faq-icon">
          {isOpen ? '-' : '+'}
        </span>
      </div>
      <div className={`faq-answer${isOpen ? '' : ' hidden'}`}>
        <p>{answer}</p>
        {includeMoodboard && (<img className="moodboard" src={moodboard} alt="Un poco de inspiración" />)}
        {includeAccommodation && <AccommodationInfo />}
      </div>
    </div>
  );
}

export default FAQItem;