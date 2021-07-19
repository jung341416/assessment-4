from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return f"Category; {self.name}"


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.title} is belonged to {self.category} and is posted by {self.poster}" 