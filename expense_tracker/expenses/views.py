from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Expense, Category, Budget
from .forms import ExpenseForm, CategoryForm, BudgetForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.db.models import Sum
import json
import calendar


@login_required
def home(request):
    expenses = []
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/home.html', context={'expenses': expenses})

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expenses:expense_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expenses:expense_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expenses/expense_confirm_delete.html'
    success_url = reverse_lazy('expenses:expense_list')

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = context['expenses']
        budgets = Budget.objects.filter(user=self.request.user)

        remaining_budget_per_category = {}
        for budget in budgets:
            remaining_budget_per_category[(budget.category.id, budget.month)] = budget.get_remaining_budget()

        for expense in expenses:
            month = expense.date.strftime('%Y-%m')
            expense.remaining_budget = remaining_budget_per_category.get((expense.category.id, month), None)

        return context

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = 'expenses/expense_detail.html'
    context_object_name = 'expense'    #the default name of the object is object_list, now renamed to expense

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'expenses/category_form.html'
    success_url = reverse_lazy('expenses:category_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'expenses/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'expenses/category_form.html'
    success_url = reverse_lazy('expenses:category_list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'expenses/category_confirm_delete.html'
    success_url = reverse_lazy('expenses:category_list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'expenses/budget_form.html'
    success_url = reverse_lazy('expenses:budget_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'expenses/budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budgets = context['budgets']
        
        for budget in budgets:
            budget.remaining_budget = budget.get_remaining_budget()
        
        return context

class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'expenses/budget_form.html'
    success_url = reverse_lazy('expenses:budget_list')

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'expenses/budget_confirm_delete.html'
    success_url = reverse_lazy('expenses:budget_list')

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
class DashboardView(TemplateView):
    template_name = 'expenses/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_month = datetime.now().strftime('%Y-%m')

        # Dashboard Expensess by Category
        category_expenses = Expense.objects.filter(
            user=self.request.user, 
            date__month=current_month.split('-')[1], 
            date__year=current_month.split('-')[0]
        ).values('category__name').annotate(total=Sum('amount'))

        expenses_data = [
            {'category__name': expense['category__name'], 'total': float(expense['total'])}
            for expense in category_expenses
        ]

        context['expenses_data'] = json.dumps(expenses_data)

        # Dashboard Monthly Spending Trend
        monthly_spending = Expense.objects.filter(
            user=self.request.user).values('date__month').annotate(total=Sum('amount')).order_by('date__month')

        monthly_spending_data = [
            {'month': calendar.month_name[entry['date__month']], 'total': float(entry['total'])}
            for entry in monthly_spending
        ]
        context['monthly_spending'] = json.dumps(monthly_spending_data)

        return context