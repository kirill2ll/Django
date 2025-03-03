from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.views.generic.edit import CreateView

@login_required
def home(request):
    expenses = []
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/home.html', context={'expenses': expenses})

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expenses:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

