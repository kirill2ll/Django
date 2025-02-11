from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']
        fields = '__all__' # pass all fields

        # custom labels
        labels = {
            'first_name': 'FIRST Name',
            'last_name': 'Last NAME',
            'stars': 'Super Stars'
        }

        error_messages = {
            'stars': {
                'required': 'Please enter the number of stars',
                'invalid': 'Please enter a number between 1 and 5',
                'min_value': 'Please enter a number between 1 and 5',
                'max_value': 'Please enter a number between 1 and 5'
            }
        }
        # widgets = {
        #     'review': forms.Textarea(attrs={'class':'myform','rows': 5, 'cols': 50})
        # }
