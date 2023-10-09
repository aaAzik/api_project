from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=230)

    def __str__(self):
        return self.title



class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.title