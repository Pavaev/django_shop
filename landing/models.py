from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class Subscriber(models.Model):
    class Meta:
        db_table = 'subscribers'
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return smart_text('№:'+str(self.id) + '\n Email:' + self.email)
