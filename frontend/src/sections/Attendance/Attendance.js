import './Attendance.css';

import AttendanceForm from '../../components/attendanceForm/AttendanceForm';
import SectionTitle from '../../components/sectionTitle/SectionTitle';


function Attendance() {
  return (
    <section className="attendance">
      <SectionTitle title="¿Te vienes?" />
      <div className="attendance-content">
        <p>
          Nos encancaría contar contigo pero, si no puedes, no nos vamos a enfadar.
          Eso sí, organizar una boda es un movidote, así que te pedimos por favor 
          que rellenes este formulario cuanto antes. 👇
        </p>
        <button>
          Reserva tu entrada
        </button>
      </div>
    </section>
  );
}

export default Attendance;

