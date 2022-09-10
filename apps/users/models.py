from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, nickname, name, password):
        user = self.model(
            nickname     = nickname,
            name         = name,
            is_superuser = 0,
            is_staff     = 0,
            is_active    = 1,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, nickname, name, password):
        user = self.create_user(
            nickname = nickname,
            name     = name,
            password = password,
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    nickname     = models.CharField(unique=True, max_length=45)
    name         = models.CharField(max_length=45)
    password     = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    date_joined  = models.DateTimeField(auto_now_add=True)
    is_staff     = models.IntegerField(blank=True, null=True)
    is_active    = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD  = 'nickname'
    REQUIRED_FIELDS = ['name']
    class Meta:
        db_table = 'auth_user'