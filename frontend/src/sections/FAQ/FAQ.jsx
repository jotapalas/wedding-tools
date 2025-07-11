import './FAQ.css';

import { useState, useEffect } from 'react';

import SectionTitle from '../../components/sectionTitle/SectionTitle';
import FAQItem from '../../components/faqItem/FAQItem';

function FAQ() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_BASE_URL;

    fetch(`${apiUrl}/info/faqs/`)
      .then((response) => response.json())
      .then((data) => {
        setQuestions(data);
      })
      .catch((error) => {
        console.error('Error fetching FAQ:', error);
      });
  }, []);

  return (
    <section className="faq">
      <SectionTitle title="FAQ" />
      <div className="faq-content">
        {questions.map((item) => (
          <FAQItem
            key={item.id}
            {...item}
          />
        ))}
      </div>
    </section>
  );
}

export default FAQ;
