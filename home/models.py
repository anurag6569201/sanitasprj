from django.db import models
from userauths.models import User

# Create your models here.
class recentUpdates(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    content=models.CharField(max_length=100)
    visitingLink=models.CharField(max_length=100)

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)