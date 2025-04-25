from django.apps import AppConfig
from django.core.management import call_command

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # Gọi command để tạo admin và role "Patient" khi ứng dụng khởi động
        import app.signals