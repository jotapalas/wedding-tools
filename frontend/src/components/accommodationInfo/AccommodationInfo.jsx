function AccommodationInfo() {
  const bookingUrl = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaEaIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Aqvnob4GwAIB0gIkNTE0Y2M1ZTUtNzM0YS00ZjBiLTg1ODMtZGYzM2E3ZDg1ZjUx2AIF4AIB&sid=a8b59fefd1d712f4fa7a5ac49582009b&aid=304142&ss=Sevilla%2C+Andalusia%2C+Espanya&efdco=1&lang=en-gb&src=index&dest_id=-402849&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=ca&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d2b96fd5cb270387&checkin=2025-09-26&checkout=2025-09-28&group_adults=2&no_rooms=1&group_children=0&nflt=di%3D1218';
  const abbaUrl = 'https://abbahoteles.com/';
  const promoCode = 'BODAROCIOYJUAN';
  const sevillaCenterUrl = 'https://www.hotelescenter.es/es/hotel-sevilla-center/';


  return (
    <div className="accommodation-info">
      <p>
        Cualquiera de&nbsp;
        <a  
          href={bookingUrl}
          target="_blank"
          rel="noopener noreferrer"
        >estos alojamientos</a> está cerca de la iglesia y de donde dejará el bus a la vuelta.
      </p>
      <p>
        Si quieres alojarte en el hotel Abba, puedes usar el código&nbsp; 
        <span className="bold">{promoCode}</span>&nbsp;
        para conseguir un descuento del 15%, pero debes reservar a través de su web:&nbsp; 
        <a href={abbaUrl} target="_blank" rel="noopener noreferrer">{abbaUrl}</a>.
      </p>
      <p>
        Por otro lado, si te haces socio del hotel Sevilla Center,&nbsp;
        también puedes conseguir un 12% de descuento en su web:&nbsp;
        <a href={sevillaCenterUrl} target="_blank" rel="noopener noreferrer">
          {sevillaCenterUrl}  
        </a>.
      </p>
    </div>
  );
}

export default AccommodationInfo;
