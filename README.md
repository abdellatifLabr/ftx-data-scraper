# Environment Setup

1. Clone repository
```
$ git clone https://github.com/abdellatifLabr/ftx-data-scraper
```

2. Install dependencies
  1. Install redis
  2. Install postgresql (create database with name `ftx`)
  3. Install pipenv
  ```
  $ pip install pipenv
  ```
  4. Set up environment
  ```
  $ pipenv --three
  ```
  5. Install packages
  ```
  $ pipenv install --dev
  ```
3. Configure th database
set database settings in `ftx_data_scraper/settings.py` in line 121 and below.
4. Migrate
5. Create `.env` file similar to `.example.env`
```
$ python manage.py migrate
```
6. Start redis server (`redis-server` command)
7. Start project server 
```
$ daphne ftx_data_scraper.asgi:application
```
8. Start celery worker
```
$ celery worker -A ftx_data_scraper -l INFO
```
9. Start celery beat
```
$ celery beat -A ftx_data_scraper -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
