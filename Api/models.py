from django.db import models
from django.db.models.fields import *
from django.core.validators import MinLengthValidator

# Create your models here.
# First name, Last Name, Email, Age, DoB, Mobile No
class User(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    age = models.IntegerField(blank=False)
    dob = models.DateField(blank=False)
    mobile_no = models.CharField(max_length = 10, blank=False, validators=[MinLengthValidator(10)])


    def __str__(self):
        return self.first_name + " "  + self.last_name