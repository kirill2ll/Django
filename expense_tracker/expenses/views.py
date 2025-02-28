from django.shortcuts import render
from .models import Expense

def home(request):
    expenses = []
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/home.html', context={'expenses': expenses})