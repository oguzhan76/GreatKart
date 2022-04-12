from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, firstName, lastName, username, email, password=None):
        if not email:
            raise ValueError('User must provide an email address')
        
        if not username:
            raise ValueError('User must provide a username')
        

        user = self.model(
            email= self.normalize_email(email),
            first_name = firstName,
            last_name = lastName,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            firstName = first_name,
            lastName = last_name,
            username = username,
            email = email,
            password = password
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name       = models.CharField(max_length=50)
    last_name        = models.CharField(max_length=50)
    username        = models.CharField(max_length=50)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number     = models.CharField(max_length=50)

    date_joined      = models.DateTimeField(default=timezone.now)
    lastLogin       = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)    
    is_active       = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True