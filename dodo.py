from doit.tools import LongRunning, Interactive


def task_build():
    return {
        'actions': [
            'pip install poetry',
            'poetry install',
            'yarn',
        ],
    }


def task_commit():
    return {
        'actions': [
            'git add --all',
            Interactive('poetry run cz c')
        ],
    }


def task_runserver():
    return {
        'actions': [
            LongRunning('python manage.py runserver_plus 0.0.0.0:8000'),
        ],
    }
