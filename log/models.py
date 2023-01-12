from django.db import models
from user.models import User


class Log(models.Model):
    class Meta:
        db_table = 'Log'
        ordering = ['-created_at']

    author=models.ForeignKey(User, on_delete = models.CASCADE, related_name='author')
    money=models.IntegerField()
    content = models.CharField(max_length=50)
    category=models.CharField(max_length=10) # 선택지
    created_at = models.DateTimeField(auto_now_add=True)
