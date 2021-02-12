release: python manage.py collectstatic && manage.py compress --force && python manage.py migrate
web: gunicorn src.wsgi --log-file -
