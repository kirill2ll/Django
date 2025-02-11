from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
        # widgets = {
        #     'review': forms.Textarea(attrs={'class':'myform','rows': 5, 'cols': 50})
        # }
