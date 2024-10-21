from datetime import date

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=20, null=True)
    num_employees = models.IntegerField(default=0)
    num_tables = models.IntegerField(default=0)
    num_chairs = models.IntegerField(default=0)

    def __str__(self):
        return self.name