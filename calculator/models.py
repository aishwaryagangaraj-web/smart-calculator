from django.db import models


class CalculationHistory(models.Model):
    category = models.CharField(max_length=50)
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.expression} = {self.result}"