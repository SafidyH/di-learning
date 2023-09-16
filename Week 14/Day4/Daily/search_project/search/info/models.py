from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name