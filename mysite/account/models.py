from django.db import models
from django.contrib.auth.models import User

class UserSessionData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_data = models.JSONField(default=dict)  # 세션 데이터를 JSON 형식으로 저장

    def __str__(self):
        return f"Session data for user {self.user.username}"
