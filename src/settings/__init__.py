from src.settings.base import *

SETTINGS = env('SETTINGS')

if SETTINGS == 'DEVELOPMENT':
    from src.settings.development import *
else:
    from src.settings.production import *

