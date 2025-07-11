#!/bin/sh

echo "Waiting for DB..."

set -e

while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
  sleep 1
done

echo "Database ready. Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn src.wsgi:application --bind 0.0.0.0:8000
