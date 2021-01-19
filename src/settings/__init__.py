from src.settings.base import *

if env('SETTINGS') == 'DEVELOPMENT':
    from src.settings.development import *
else:
    from src.settings.production import *
