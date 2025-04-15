import "./AddToCalendarButton.css";

import React from "react";

import { useState } from "react";


const AddToCalendarButton = () => {
  const [showOptions, setShowOptions] = useState(false);

  const event = {
    title: "Boda Rocío y Juan",
    description: "Iglesia Santa María de la Paz",
    location: "C. Bustos Tavera, 15, Casco Antiguo, 41003 Sevilla",
    startDate: new Date("2025-09-27T18:30:00"),
    endDate: new Date("2025-09-28T05:30:00"),
  }

  const formatDate = (date) => {
    return date.toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
  };

  const downloadICS = () => {
    const icsContent = `
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:${event.title}
DESCRIPTION:${event.description}
LOCATION:${event.location}
DTSTART:${formatDate(event.startDate)}
DTEND:${formatDate(event.endDate)}
END:VEVENT
END:VCALENDAR
    `.trim();

    const blob = new Blob([icsContent], { type: "text/calendar;charset=utf-8" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "boda_rocio_y_juan.ics";
    a.click();
    URL.revokeObjectURL(url);
  };

  const openGoogleCalendar = () => {
    const url = `https://www.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(
      event.title
    )}&details=${encodeURIComponent(event.description)}&location=${encodeURIComponent(
      event.location
    )}&dates=${formatDate(event.startDate)}/${formatDate(event.endDate)}`;
    window.open(url, "_blank");
  };

  return <div className="add-to-calendar-button">
          <button onClick={() => setShowOptions(!showOptions)}>
            Añadir al calendario
          </button>
          {showOptions && (
            <div className="calendar-options">
              <div
                className="calendar-option"
                onClick={() => {
                  openGoogleCalendar();
                  setShowOptions(false);
                }}
              >
                📆 Añadir a Google Calendar
              </div>
              <div
                className="calendar-option"
                onClick={() => {
                  downloadICS();
                  setShowOptions(false);
                }}
              >
                📄 Descargar archivo (.ics)
              </div>
            </div>
          )}
        </div>;
};

export default AddToCalendarButton;
