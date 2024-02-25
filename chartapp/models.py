from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    expense = models.IntegerField()
    income = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.category} - {self.expense} - {self.income} - {self.date}'
    