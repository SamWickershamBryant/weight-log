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
curl -X POST http://localhost:8000/api-auth/weight-entry/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjE5MjUzLCJpYXQiOjE2ODcyMTg5NTMsImp0aSI6IjliYTlkMzk3OWViYzRmZDU4ZTNiMDlhYzdlN2NiODNhIiwidXNlcl9pZCI6MX0.57K7Fw--5UjG_UZa-5rUPNb9irqhHRQqqCUfTOfCHGc' -H "Content-Type: application/json" -d '{"weight": 120}'
curl -X GET http://localhost:8000/api-auth/all-weights/ -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjIwNjQ1LCJpYXQiOjE2ODcyMjAzNDUsImp0aSI6Ijc1ZWY3NDZkYWQ1YjRjZjk4YTQxN2U5YzA4ZjU5NzViIiwidXNlcl9pZCI6MX0.tLHt5qtSGvnj_11nicQ9StUt7Oc6qG_vAkhngXuXA3U'
curl -X GET http://localhost:8000/api-auth/all-weights/ \
    curl -X GET http://localhost:8000/api-auth/all-weights/ \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjIxNzU0LCJpYXQiOjE2ODcyMTgxNzYsImp0aSI6ImFlYjYyZjdhMGJlMTQ2NTE4YmM0NTRlMjBjYzZiZTgyIiwidXNlcl9pZCI6MX0.k4Y1VYOd0BGBdltUaLAyLsVEPkWzoq-oa6E-6Iruf10'

-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjIwNjQ1LCJpYXQiOjE2ODcyMjAzNDUsImp0aSI6Ijc1ZWY3NDZkYWQ1YjRjZjk4YTQxN2U5YzA4ZjU5NzViIiwidXNlcl9pZCI6MX0.tLHt5qtSGvnj_11nicQ9StUt7Oc6qG_vAkhngXuXA3U' \

{
"username":"jim",
"password":"Password1231",
"email":"123@gmail.com",
"first_name":"jim",
"last_name":"diamond"
}

{
"username":"jim",
"password":"Password1231"
}

"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzMwNDU3NiwiaWF0IjoxNjg3MjE4MTc2LCJqdGkiOiJkM2M5MGUzMTU2ZjI0NDQ5YTNlMDRlYTIxNGIyZWM2NiIsInVzZXJfaWQiOjF9.awmOMy2qLXJn5vQ8BoK8RtysYgzlMWPx6ka-8vj5OkM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MjE4NDc2LCJpYXQiOjE2ODcyMTgxNzYsImp0aSI6IjkzNmE3NzVjMGUyMjQ2M2NhZmZjY2ZhMGYxMDcwZmRjIiwidXNlcl9pZCI6MX0.GJO9bI76uOXHTuSIcnGTGPLFtFCtpwiBjcHaBUQe6Vs"
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