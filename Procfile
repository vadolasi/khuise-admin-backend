release: python manage.py collectstatic && python manage.py migrate
web: gunicorn src.wsgi --log-file -
