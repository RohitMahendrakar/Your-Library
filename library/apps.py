from django.apps import AppConfig

#The AppConfig class used to configure the application has a path class attribute, which is the absolute directory path Django will use as the single base path for the application.
class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
