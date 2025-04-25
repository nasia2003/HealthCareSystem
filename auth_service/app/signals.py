from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
from app.models import RoleCus

@receiver(post_migrate)
def create_default(sender, **kwargs):
    if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='adminpassword',  # Thay đổi mật khẩu cho phù hợp
                email='admin@example.com'
            )

        # Tạo role "Patient" nếu chưa có
    if not RoleCus.objects.filter(name='Patient').exists():
        RoleCus.objects.create(name='Patient', description='Role for patients')