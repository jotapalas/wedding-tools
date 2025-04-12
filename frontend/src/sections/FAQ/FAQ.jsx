import './FAQ.css';

import SectionTitle from '../../components/sectionTitle/SectionTitle';
import FAQItem from '../../components/faqItem/FAQItem';

function FAQ() {
    const questions = [
        {
            question: "¿Puedo comprar un producto sin registrarme?",
            answer: "Sí, puedes comprar sin registrarte. Sin embargo, te recomendamos que te registres para facilitar futuras compras y acceder a promociones exclusivas."
        },
        {
            question: "¿Cuáles son los métodos de pago aceptados?",
            answer: "Aceptamos tarjetas de crédito, débito, PayPal y transferencias bancarias."
        },
        {
            question: "¿Cómo puedo rastrear mi pedido?",
            answer: "Una vez que tu pedido haya sido enviado, recibirás un correo electrónico con un enlace de seguimiento."
        },
        {
            question: "¿Puedo devolver un producto?",
            answer: "Sí, puedes devolver un producto dentro de los 30 días posteriores a la compra. Asegúrate de que esté en su estado original."
        },
    ];
    return (
        <div className="faq">
        <SectionTitle title="FAQ" />
        <div className="faq-content">
            {questions.map((item, index) => (
                <FAQItem key={index} question={item.question} answer={item.answer} />
            ))}
        </div>
        </div>
    );
}

export default FAQ;
