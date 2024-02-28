from django.db import models

# Create your models here.
class recentUpdates(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    content=models.CharField(max_length=100)
    visitingLink=models.CharField(max_length=100)