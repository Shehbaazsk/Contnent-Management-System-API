from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from .constants import USER_ROLES
# Create your models here.

""""" We can also make that tables to reduce redundancy but I'm making it simple"""
# class Country(models.Model):
#     name = models.CharField(max_length=255, unique=True)

# class State(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

# class City(models.Model):
#     name = models.CharField(max_length=255)
#     state = models.ForeignKey(State, on_delete=models.CASCADE) 

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255, unique=True)
    mobile_no=models.IntegerField()
    user_role = models.CharField(max_length=20, choices=USER_ROLES.choices, default=USER_ROLES.AUTHOR)
    address = models.TextField(null=True, blank=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.PositiveIntegerField()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"




    objects=UserManager()   

    USERNAME_FIELD = 'email'    

    def __str__(self):
        return self.email
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"