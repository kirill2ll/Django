from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Write your review here', widget=forms.Textarea(attrs={'class':'myform','rows': 5, 'cols': 50}))