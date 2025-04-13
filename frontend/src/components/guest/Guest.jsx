import './Guest.css';

function Guest({ guest, onClick }) {
    return (
        <div className="guest">
            <div className="guest-info">
                {guest.first_name} {guest.last_name}
            </div>
            <button className="guest-button" onClick={onClick}>Confirmar</button>
        </div>
    );
}

export default Guest;
