from django.db import models
from django.contrib.auth.models import User
from reader.models import Story
from django.utils import timezone
from myaccount.models import Profile

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #story = models.ForeignKey(Story, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    story_title = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.title
