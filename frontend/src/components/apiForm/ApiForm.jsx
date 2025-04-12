import React, { useState, useEffect } from 'react';
import './ApiForm.css';


const ApiForm = ({ className = 'api-form', url, fields, method = 'POST', initialData = {}, onSuccess, onError }) => {
  const [formData, setFormData] = useState({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const initialFormData = fields.reduce((acc, field) => {
      acc[field.name] = initialData[field.name] ?? '';
      return acc;
    }, {});
    setFormData(initialFormData);
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      let request = {};
      if (method === 'GET') {
        const params = new URLSearchParams(formData).toString();
        url += `?${params}`;
        request = {
          method
        };
      } else {
        request =  {
          method,
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
        }
      }
      const response = await fetch(url, request);
      const result = await response.json();

      if (response.ok) {
        onSuccess?.(result);
      } else {
        onError?.(result);
      }
    } catch (err) {
      onError?.(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className={className}>
      {fields.map(({ name, type, label, className, required, options }) => (
        <div key={name} className="form-group">
          <label>{label || name}</label>
          {type === 'select' ? (
            <select
              name={name}
              value={formData[name] ?? ''}
              onChange={handleChange}
              className={className || 'input-field'}
              required={required}
            >
              <option value="">Selecciona una opción</option>
              {options?.map((opt) => (
                <option key={opt.value} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          ) : (
            <input
              type={type}
              name={name}
              value={formData[name] ?? ''}
              className={className || 'input-field'}
              onChange={handleChange}
              required={required}
            />
          )}
        </div>
      ))}
      <button
        type="submit"
        disabled={loading}
      >
        {loading ? 'Enviando...' : 'Enviar'}
      </button>
    </form>
  );
};

export default ApiForm;
