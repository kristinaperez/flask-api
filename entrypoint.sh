#!/bin/sh

echo "⏳ Waiting for database..."

# ждём пока postgres поднимется
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "✅ Database is up"

echo "⚙️ Running DB init..."
python -c "from app import init_db; init_db()"

echo "🚀 Starting Gunicorn..."
exec gunicorn -w 4 -b 0.0.0.0:5000 app:app
