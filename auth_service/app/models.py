import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

class RoleCus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, username, fullname, password=None, role=None):
        if not email:
            raise ValueError("Users must have an email address")
        role = RoleCus.objects.get(name="Patient")
        user = self.model(email=self.normalize_email(email), username=username, fullname=fullname, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, fullname, password):
        user = self.create_user(email, username, fullname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserCus(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    role = models.ForeignKey(RoleCus, on_delete=models.SET_NULL, null=True)

    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname']

    groups = models.ManyToManyField(
        Group,
        related_name='usercus_set',  # Thay đổi related_name
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name='usercus'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usercus_set',  # Thay đổi related_name
        blank=True,
        help_text="Specific permissions for this user."
    )

    def set_password(self, raw_password):
        super().set_password(raw_password)

    def __str__(self):
        return self.email
