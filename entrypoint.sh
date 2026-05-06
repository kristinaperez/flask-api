 #!/bin/sh

echo "⏳ Waiting for database at $DB_HOST:$DB_PORT..."

MAX_RETRIES=30
COUNT=0

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
  COUNT=$((COUNT+1))
  if [ $COUNT -ge $MAX_RETRIES ]; then
    echo "❌ Database not available"
    exit 1
  fi
done

echo "✅ Database is up"

echo "⚙️ Running DB init..."
python -c "from app import init_db; init_db()" || exit 1

echo "🚀 Starting Gunicorn..."
exec gunicorn \
  -w 4 \
  -b 0.0.0.0:5000 \
  --timeout 30 \
  --log-level info \
  app:app
  
