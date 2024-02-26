from django.db import models
from userauths.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, default="user")
    surname = models.CharField(max_length=100, default="1234")
    mobile_number = models.CharField(max_length=15, default="XXXXXXXXXX")
    address = models.CharField(max_length=255, default="No Address Provided")
    postcode = models.CharField(max_length=20, default="XXXXXX")
    area = models.CharField(max_length=100, default="Unknown Area")
    email = models.EmailField(default="example@example.com")
    education = models.CharField(max_length=255, default="No Education Information")
    country = models.CharField(max_length=100, default="Unknown Country")
    state_region = models.CharField(max_length=100, default="Unknown Region")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Sanitizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sanitizer')
    name=models.CharField(max_length=100,default="Aims Hospital")
    street = models.CharField(max_length=255, default="Street 99")
    city = models.CharField(max_length=100, default="City 99")
    state = models.CharField(max_length=100, default="State 99")
    zip = models.CharField(max_length=20, default="XXXXXX")
    contactperson=models.CharField(max_length=100,default="Virju")
    phone = models.CharField(max_length=10, default="XXXXXXXXXX")
    email = models.EmailField(default="example@example.com")

    certificate=models.ImageField(upload_to='sanitizerDoc/', null=True, blank=True)
    isChecked=models.BooleanField(default=True)
    isSubmitted=models.BooleanField(default=False)

    is_verified=models.BooleanField(default=False)
