from invoke import task


@task
def build(cmd):
    cmd.run('pip install poetry')
    cmd.run('poetry install')


@task
def run(cmd):
    cdm.run('python manage.py runserver_plus 0.0.0.0:8000')

