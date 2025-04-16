import './AttendanceForm.css';
import ApiForm from '../apiForm/ApiForm';
import AddToCalendarButton from '../addToCalendarButton/AddToCalendarButton';

import { useState } from 'react';
import { useEffect } from 'react';

import SectionTitle from '../sectionTitle/SectionTitle';
import Guest from '../guest/Guest';
import AccommodationInfo from '../accommodationInfo/AccommodationInfo';


function AttendanceForm({ className, onClose = null }) {
    const [currentGuest, setCurrentGuest] = useState();
    const [loading, setLoading] = useState(true);
    const [stage, setStage] = useState(1);
    const [guests, setGuests] = useState([]);

    const apiUrl = import.meta.env.VITE_API_BASE_URL;

    const params = new URLSearchParams(window.location.search);
    const guestId = params.get('guestId');
    
    useEffect(() => {
        if (!guestId) {
            setLoading(false);
            return;
        }
        fetch(`${apiUrl}/guests/guest/${guestId}/`)
        .then((response) => response.json())
        .then((data) => {
            setCurrentGuest(data);
            setLoading(false);
        })
        .catch((error) => {
            setLoading(false);
        });
    }, []);

    const selectGuest = (guest) => {
        setCurrentGuest(guest);
        setStage(3);
    }

    const handleFinish = () => {
        const isAttending = currentGuest.attending === 1;
        const nextStage = isAttending ? 5 : 1;
        if (!isAttending && onClose) {
            onClose();
            return;
        }
        setStage(nextStage);
    };

    let content = <div className="loading">Loading...</div>;
    
    if (loading) {
        return content;
    }

    if (stage === 1) {
        const handleSuccess = (data) => {
            setGuests(data);
            setStage(2);
        };
        const handleError = (error) => {
            setGuests([]);
            setStage(2);
        };
        content = <div className="attendance-form">
            <SectionTitle title="Búscate en la lista" />
            <p className="attendance-form-instructions">
                Por favor, introduce tu nombre y/o apellido para encontrarte en la lista de invitados.
            </p>
            <ApiForm
                url={`${apiUrl}/guests/search/`}
                method="GET"
                fields={[
                    { name: 'first_name', type: 'text', label: 'Nombre' },
                    { name: 'last_name', type: 'text', label: 'Apellido' },
                ]}
                onSuccess={handleSuccess}
                onError={handleError}
            />
        </div>;
    } else if (stage === 2) {
        content = <div className="confirmation-message">
            <SectionTitle title={
                guests.length === 0
                ? 'No se encontraron invitados'
                : 'Invitados encontrados'
                
            } />
            <div className="guests-container">
                {guests.map((guest) => (
                    <Guest
                        key={guest.id}
                        guest={guest}
                        onClick={() => selectGuest(guest)} 
                    />
                ))}
            </div>
            <button onClick={() => {
                setStage(1);
                setGuests([]);
            }}>Volver</button>
        </div>;
    } else if (stage === 3) {
        const handleSuccess = (data) => {
            setStage(4);
            setCurrentGuest(data);
        }
        const handleError = (error) => {
            console.error(error);
            setStage(1);
        }
        content = <div className="confirmation-message">
            <SectionTitle title="Confirma tu asistencia y preferencias" />
            <ApiForm
                url={`${apiUrl}/guests/guest/${currentGuest.id}/`}
                method="PATCH"
                fields={[
                    { name: 'first_name', type: 'text', label: 'Nombre', required: true },
                    { name: 'last_name', type: 'text', label: 'Apellido', required: true },
                    { name: 'email', type: 'text', label: 'Correo electrónico' },
                    { name: 'attending', type: 'select', label: 'Asistiré', options: [
                        {value: 1, label: 'Sí'},
                        {value: 0, label: 'No'},
                    ], required: true, horizontal: true},
                    { name: 'special_diet', type: 'select', label: 'Dieta especial', options: [
                        {value: '', label: 'Ninguna'},
                        {value: 'vegetarian', label: 'Vegetariana'},
                        {value: 'vegan', label: 'Vegana'},
                        {value: 'pregnant', label: '¡Estoy preñator!'},
                    ], horizontal: true},
                    { name: 'allergies', type: 'text', label: 'Alergias' },
                    { name: 'needs_transport', type: 'select', label: '¿Necesitas autobús?', options: [
                        {value: true, label: 'Sí'},
                        {value: false, label: 'No'},
                    ], horizontal: true, required: true},
                    { name: 'needs_accommodation', type: 'select', label: '¿Necesitas info sobre alojamiento?', options: [
                        {value: true, label: 'Sí'},
                        {value: false, label: 'No'},
                    ], horizontal: true},
                    { name: 'pre_wedding', type: 'select', label: '¿Te apuntas a la preboda?', options: [
                        {value: 1, label: 'Sí'},
                        {value: 0, label: 'No'},
                        {value: 2, label: 'No sé todavía'},
                    ], horizontal: true, required: true},
                ]}
                onSuccess={handleSuccess}
                onError={handleError}
                initialData={currentGuest}
            />
        </div>;
    } else if (stage === 4) {
        content = <div className="confirmation-message">
            <SectionTitle title="¡GRACIAS!" />
            <h3 className="attendance-form-instructions">
                {
                    currentGuest.attending === 1
                    ? '¡Nos vemos en la boda!'
                    : '¡Ooooh! ¡Pues nos vemos en los bares!'
                }
            </h3>
            {
                currentGuest.attending === 1 &&
                <div className="add-to-calendar-container">
                    <AddToCalendarButton />
                </div>
            }
            {
                currentGuest.same_group_guests.length > 0
                ? <div className="same-group-guests">
                    <p className="attendance-form-instructions">
                        ¡Hay invitados en tu grupo que no han contestado todavía!
                    </p>
                    <p className="attendance-form-instructions">
                        ¿Quieres rellenar el formulario por ellos?
                    </p>
                    <button onClick={() => {
                        setGuests(currentGuest.same_group_guests);
                        setStage(2);
                    }}>Sí</button>
                    <button onClick={() => handleFinish()}>No, terminar</button>
                </div>
                : <button onClick={() => {handleFinish()}}>
                    Terminar
                </button>
            }
        </div>;
    } else if (stage === 5) {
        const spotifyUrl = import.meta.env.VITE_SPOTIFY_PLAYLIST_URL;
        if (!spotifyUrl) {
            if (onClose) {
                onClose();
            }
            setStage(1);
            return;
        }
        
        content = <div className="confirmation-message">
            <SectionTitle title="Una última cosa..." />
            <p className="attendance-form-instructions">
                Hemos creado una lista de Spotify colaborativa 
                y nos encantaría que añadieras <span className="bold">tu canción favorita</span> para la fiesta.
            </p>
            <p className="attendance-form-instructions">
            <span className="bold">No podemos prometerte que suene,</span> pero tendremos en cuenta los gustos generales.
            </p>
            <button onClick={() => {
                window.open(spotifyUrl, '_blank');
            }}>
                ¡Por supuesto!
            </button>

            {
                currentGuest.needs_accommodation === true &&
                <div className="accomodation-info-container">
                    <SectionTitle title="Sobre el alojamiento" />
                    <AccommodationInfo />
                </div>
            }
        </div>;
    }

    return <div className={className || 'attendance-form-content'}>
        {content}
    </div>;
}


export default AttendanceForm;