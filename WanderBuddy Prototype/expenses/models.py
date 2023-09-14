from django.db import models
from tripmgmt.models import Participant, Trip

class Expense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    payer = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='expenses_paid')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.description} ({self.trip.title})"