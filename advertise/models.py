from django.db import models

# Create your models here.
class advertisement(models.Model):
    image = models.ImageField(upload_to='advertisement/',null=True, blank=True)

class sponsor(models.Model):
    image = models.ImageField(upload_to='sponsor/',null=True, blank=True)

class partnership(models.Model):
    image = models.ImageField(upload_to='partnership/',null=True, blank=True)