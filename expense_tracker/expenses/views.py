from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense

@login_required
def home(request):
    expenses = []
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/home.html', context={'expenses': expenses})
