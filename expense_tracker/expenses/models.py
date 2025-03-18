from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.amount} on {self.date}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # start_date = models.DateField()
    # end_date = models.DateField()
    month = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.amount} from {self.month}"

    def get_remaining_budget(self):
        year, month = map(int, self.month.split('-'))

        total_expenses = Expense.objects.filter(
            user=self.user,
            category=self.category,
            date__year=year,
            date__month=month).aggregate(total=Sum('amount'))['total'] or 0

        remaining_budget = self.amount - total_expenses

        return remaining_budget