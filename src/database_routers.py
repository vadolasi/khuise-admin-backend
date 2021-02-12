from django.conf import settings


class DatabaseAppsRouter:
    def db_for_read(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label, None)

    def db_for_write(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label, None)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in settings.DATABASE_APPS_MAPPING.values():

            return settings.DATABASE_APPS_MAPPING.get(app_label) == db

        elif app_label in settings.DATABASE_APPS_MAPPING:

            return False

        return None

