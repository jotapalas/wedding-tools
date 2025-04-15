import './Attendance.css';

import { useState } from 'react';

import AttendanceForm from '../../components/attendanceForm/AttendanceForm';
import SectionTitle from '../../components/sectionTitle/SectionTitle';


function Attendance() {
  const [showForm, setShowForm] = useState(false);
  const [scrollY, setScrollY] = useState(0);
  
  const blockScroll = () => {
    const newScrollY = window.scrollY;
    setScrollY(newScrollY);
    document.body.style.position = 'fixed';
    document.body.style.top = `-${newScrollY}px`;
    document.body.style.overflow = 'hidden';
  }

  const unblockScroll = () => {
    document.body.style.position = '';
    document.body.style.overflow = '';
    window.scrollTo(0, scrollY);
  }

  const toggleForm = () => {
    const newShowForm = !showForm;
    setShowForm(newShowForm);
    if (newShowForm) {
      blockScroll();
    } else {
      unblockScroll();
    }

  }

  return (
    <section className="attendance">
      <SectionTitle title="¿Te vienes?" />
      <div className={`attendance-form-container ${showForm ? 'show' : 'hide'}`}>
        <div className="attendance-form-close" onClick={() => toggleForm()}>
          <p>X</p>
        </div>
        <AttendanceForm onClose={toggleForm} />
      </div>
      <div className="attendance-content">
        <p>
          Nos encancaría contar contigo pero, si no puedes, <span className="bold">no nos vamos a enfadar. </span>
        </p>
        <p>
          Eso sí, organizar una boda es un movidote, así que te pedimos <span className="bold">por favor </span>
          que rellenes este formulario cuanto antes, y nos digas si vienes o no.
        </p>
        <p>
          👇
        </p>
        <button
          onClick={() => toggleForm()}
          className="attendance-button"
        >
          <p>Reserva tu entrada</p>
          <p>🍸🍟🪩</p>
        </button>
      </div>
    </section>
  );
}

export default Attendance;

