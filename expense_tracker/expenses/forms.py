from django import forms
from .models import Expense, Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'description', 'category']
        labels = {
            'amount': 'Amount',
            'date': 'Date',
            'description': 'Description',
            'category': 'Category'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Name'
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Category.objects.filter(user=user)