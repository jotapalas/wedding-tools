import './App.css';
import Hero from './sections/Hero/Hero';
import Claim from './sections/Claim/Claim';
import LineUp from './sections/LineUp/LineUp';
import Attendance from './sections/Attendance/Attendance';
import Directions from './sections/Directions/Directions';
import FAQ from './sections/FAQ/FAQ';
import Gifts from './sections/Gifts/Gifts';


function App() {
  return (
    <div className="App">
      <Hero />
      <Claim />
      <LineUp />
      <Attendance />
      <Directions />
      <FAQ />
      <Gifts />
    </div>
  );
}

export default App;
