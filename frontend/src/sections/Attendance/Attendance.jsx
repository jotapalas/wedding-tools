import './Attendance.css';

import AttendanceForm from '../../components/attendanceForm/AttendanceForm';
import SectionTitle from '../../components/sectionTitle/SectionTitle';


function Attendance() {
  return (
    <section className="attendance">
      <SectionTitle title="¿Te vienes?" />
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
        <button>
          <p>Reserva tu entrada</p>
          <p>🍸🍟🪩</p>
        </button>
      </div>
    </section>
  );
}

export default Attendance;

