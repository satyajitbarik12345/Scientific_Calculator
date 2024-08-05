from django.db import models

class CalculationHistory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    operation = models.CharField(max_length=255)
    result = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.timestamp} - {self.operation}: {self.result}"
