from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    link = models.CharField(max_length = 500)
    date = models.DateTimeField(default = timezone.now())
    description = models.TextField()
    keyword = models.CharField(max_length = 50)
    category = models.ForeignKey(Category, on_delete = models.SET_DEFAULT, default = 3)
    def __str__(self):
        return self.name