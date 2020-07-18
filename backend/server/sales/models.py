from django.db import models


# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birthday = models.DateField()
    hire_date = models.DateField()


class Report(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    period = models.DateField()
    volume = models.DecimalField(decimal_places=2, max_digits=11)
