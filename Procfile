release: python manage.py migrate
web: daphne ftx_data_scraper.asgi:application --port $PORT --bind 0.0.0.0 -v2 --proxy-headers
celery: celery worker -A ftx_data_scraper -l INFO -B