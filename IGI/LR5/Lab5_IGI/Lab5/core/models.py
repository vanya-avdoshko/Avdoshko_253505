from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    is_customer = models.BooleanField('is_customer', default=False)
    is_employee = models.BooleanField('is_employee', default=False)
    is_admin = models.BooleanField('is_admin', default=False)
    phone = models.CharField('phone', max_length=20, blank=True, null=True)
    date_of_birth = models.DateField('date_of_birth', blank=True, null=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #date_of_birth = models.DateField('date_of_birth', default=False)    
    phone = models.CharField(max_length=20)
    is_regular_customer = models.BooleanField('is_regular_customer', default=False)
    is_first_time = models.BooleanField('is_first_time', default=True)
    address = models.TextField('address', blank=True, null=True)



    def __str__(self):
        return f"{self.user.username}"
    
    
    
    
    


