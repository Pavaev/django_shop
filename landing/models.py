from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return smart_text(self.email)
