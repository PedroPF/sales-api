from django.db import models


# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    birthday = models.DateField()
    hire_date = models.DateField(verbose_name='Hiring Date')

    def __str__(self):
        return self.name


class Report(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    period = models.DateField(verbose_name='Reference Period')
    volume = models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Sales Volume')

    def __str__(self):
        return f"{self.agent.name}: {self.period.strftime('%b/%y')}"

    class Meta:
        unique_together = ['agent', 'period']
