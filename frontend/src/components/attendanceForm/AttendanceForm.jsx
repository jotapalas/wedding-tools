import './AttendanceForm.css';
import ApiForm from '../apiForm/ApiForm';

import { useState } from 'react';
import { useEffect } from 'react';

function AttendanceForm() {
    const [currentGuest, setCurrentGuest] = useState();
    const [loading, setLoading] = useState(true);
    const [stage, setStage] = useState(1);
    const [guests, setGuests] = useState([]);

    const apiUrl = import.meta.env.VITE_BASE_API_URL;

    const params = new URLSearchParams(window.location.search);
    const guestId = params.get('guestId');
    console.log(guestId);
    
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
            console.error('Error fetching guest:', error);
            setLoading(false);
        });
    }, []);

    

    const selectGuest = (guest) => {
        setCurrentGuest(guest);
        setStage(3);
    }

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
            console.error('Error searching guests:', error);
            setStage(0);
        };
        content = <div className="attendance-form">
            <h2>Busca tu nombre</h2>
            <p>Por favor, ingresa tu nombre y apellido para confirmar tu asistencia.</p>
            <ApiForm
                url={`${apiUrl}/guests/search/`}
                method="GET"
                fields={[
                    { name: 'first_name', type: 'text', label: 'Nombre' },
                    { name: 'last_name', type: 'text', label: 'Apellido' },
                    { name: 'nickname', type: 'text', label: 'Apodo' },
                ]}
                onSuccess={handleSuccess}
                onError={handleError}
            />
        </div>;
    } else if (stage === 2) {
        content = <div className="confirmation-message">
            {
                guests.length === 0
                ? 'No se encontraron invitados'
                : 'Invitados encontrados:'
                
            }
            <ul>
                {guests.map((guest) => (
                    <li key={guest.id}>
                        {guest.first_name} {guest.last_name} {guest.nickname ? ` (${guest.nickname})` : ''}
                        <button onClick={() => selectGuest(guest)}>Confirmar</button>
                    </li>
                ))}
            </ul>
        </div>;
    } else if (stage === 3) {
        const handleSuccess = (data) => {
            setStage(4);
            setCurrentGuest(data);
        }
        const handleError = (error) => {
            console.error('Error updating guest:', error);
            setStage(0);
        }
        content = <div className="confirmation-message">
            <ApiForm
                url={`${apiUrl}/guests/guest/${currentGuest.id}/`}
                method="PATCH"
                fields={[
                    { name: 'first_name', type: 'text', label: 'Nombre' },
                    { name: 'last_name', type: 'text', label: 'Apellido' },
                    { name: 'nickname', type: 'text', label: 'Apodo' },
                    { name: 'attending', type: 'select', label: 'Asistiré', options: [
                        {value: 1, label: 'Sí'},
                        {value: 0, label: 'No'},
                    ]},
                ]}
                onSuccess={handleSuccess}
                onError={handleError}
                initialData={currentGuest}
            />
            <button onClick={() => {
                setStage(1);
                setCurrentGuest(null);
            }}>¿No eres tú?</button>
        </div>;
    } else if (stage === 4) {
        content = <div className="confirmation-message">
            <h2>Gracias por confirmar tu asistencia, {currentGuest.nickname || currentGuest.first_name}</h2>
            <p>Tu asistencia ha sido registrada.</p>
            {
                currentGuest.same_group_guests.length > 0 &&
                <div className="same-group-guests">
                    <h3>¿Quieres confirmar la asistencia de alguien de tu grupo?</h3>
                    <button onClick={() => {
                        setGuests(currentGuest.same_group_guests);
                        setStage(2);
                    }}>Sí</button>
                </div>
            }
            <button onClick={() => setStage(0)}>Volver</button>
        </div>;
    }

    return <div className="attendance-form-container">
        <div className="attendance-form-content">
            {content}
        </div>
    </div>;
}


export default AttendanceForm;