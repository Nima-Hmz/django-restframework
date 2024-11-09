from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title