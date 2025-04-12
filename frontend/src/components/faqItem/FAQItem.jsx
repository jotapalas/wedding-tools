import './FAQItem.css';

import { useState } from 'react';

function FAQItem({ question, answer }) {
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
      <div className={`faq-answer${isOpen ? '' : ' hidden'}`}>{answer}</div>
    </div>
  );
}

export default FAQItem;