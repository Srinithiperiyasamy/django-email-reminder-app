from django.apps import AppConfig
import threading

class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def ready(self):
        from .email_scheduler import start_email_scheduler
        threading.Thread(target=start_email_scheduler, daemon=True).start()
