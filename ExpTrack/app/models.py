from django.db import models

# Create your models here.
class Expense(models.Model):
    Titles = models.CharField(max_length=200)
    Amount = models.FloatField()
    Date = models.DateTimeField()
    Remarks = models.TextField(blank=True)
    def __str__(self):
        return self.Titles