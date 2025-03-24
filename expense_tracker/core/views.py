from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from expenses.models import Expense, Budget
from django.db.models import Sum
from datetime import datetime

def home(request):
    current_month = datetime.now().strftime('%Y-%m')

    total_expenses = Expense.objects.filter(
        user=request.user, 
        date__month=current_month.split('-')[1], 
        date__year=current_month.split('-')[0]
    ).aggregate(total=Sum('amount'))['total'] or 0

    budget = Budget.objects.filter(
        user=request.user, 
        month=current_month
    ).first()

    remaining_budget = budget.amount - total_expenses if budget else 0

    context = {
        'total_expenses': total_expenses,
        'remaining_budget': remaining_budget
    }
    return render(request, 'core/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #logs the user in after signing up
            return redirect('core:home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})