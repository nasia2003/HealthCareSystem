from django.apps import AppConfig
from django.core.management import call_command

class AuthenicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
        # Gọi command để tạo admin và role "Patient" khi ứng dụng khởi động
        call_command('seeding')