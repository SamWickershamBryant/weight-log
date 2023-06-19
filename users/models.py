from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an emai address')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

"""
{
"username":"jim",
"password":"Password1231",
"email":"123@gmail.com",
"first_name":"jim",
"last_name":"diamond"
}
"""

class User(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=25, unique=True)
    fist_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    objects = CustomUserManager()

    def has_perm(self, perm: str, obj = None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'