from django.db import models
from django.utils import timezone

# Create your models here.
class Email(models.Model):
    address = models.CharField(max_length = 50)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    date = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.title