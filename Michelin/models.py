from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    link = models.CharField(max_length = 500)
    description = models.TextField()
    keyword = models.CharField(max_length = 50)
    category = models.ForeignKey(Category, on_delete = models.SET_DEFAULT, default = 3)