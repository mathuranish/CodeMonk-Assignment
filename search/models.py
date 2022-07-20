from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Paragraph(models.Model):
    paragraph = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="para")

    def __str__(self) -> str:
        return self.paragraph
