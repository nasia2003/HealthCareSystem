from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authentication.models import RoleCus

class Command(BaseCommand):
    help = 'Create admin user and Patient role if they don\'t exist'

    def handle(self, *args, **kwargs):
        # Tạo tài khoản admin nếu chưa có
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='adminpassword',  # Thay đổi mật khẩu cho phù hợp
                email='admin@example.com'
            )

        # Tạo role "Patient" nếu chưa có
        if not RoleCus.objects.filter(name='Patient').exists():
            RoleCus.objects.create(name='Patient', description='Role for patients')