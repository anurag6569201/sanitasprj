from django.db import models
from userauths.models import User,UserProfile
from django_ckeditor_5.fields import CKEditor5Field
from plofile.models import Sanitizer

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

class spherepost(models.Model):
    content=CKEditor5Field(config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sphere_author')

    likes = models.ManyToManyField(User, related_name='event_likes', blank=True)

    def like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)