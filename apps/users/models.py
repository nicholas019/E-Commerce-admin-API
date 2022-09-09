from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils import timezone


class UserManager(BaseUserManager):
    
    def create_user(self, name, password):
        user = self.model(
            name         = name,
            is_superuser = 0,
            is_staff     = 0,
            is_active    = 1,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, password):
        user = self.create_user(
            name     = name,
            password = password,
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name         = models.CharField(unique=True, max_length=45)
    password     = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    date_joined  = models.DateTimeField(auto_now_add=True)
    is_staff     = models.IntegerField(blank=True, null=True)
    is_active    = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD  = 'name'
    REQUIRED_FIELDS = ['city']

    class Meta:
        db_table = 'auth_user'


class DeliveryInfo(models.Model):
    user          = models.ForeignKey("users.User", on_delete=models.CASCADE)
    country_code  = models.CharField(max_length=45)
    country_dcode = models.CharField(max_length=45)
    country_name  = models.CharField(max_length=45)
    city_name     = models.CharField(max_length=45)

    class Meta:
        db_table = 'delivery_info'
