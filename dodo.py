import os
from pathlib import Path
import fnmatch

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


def task_realese():
    pug_files = []

    for root, dirnames, filenames in os.walk('templates'):
        for filename in fnmatch.filter(filenames, '*.pug'):
            pug_files.append(Path(root, filename))

    commands = []

    for pug_file in pug_files:
        html_file = pug_file.parent / (pug_file.stem + '.html')
        command = f'pypugjs -c django {pug_file} {html_file}'

        if str(pug_file.parent) == 'email':
            command += ' && mjml {html_file} -o {html_file}'

        commands.append(command)

    return {
        'actions': commands,
    }

