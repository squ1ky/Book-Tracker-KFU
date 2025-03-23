from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Читаю'),
        ('finished', 'Прочитано'),
        ('to_read', 'Хочу прочитать')
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_read')
    added_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
