from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #success_url
    success_url = '/classroom/thank_you/'
    # success_url = reverse_lazy('classroom:thank_you')  #reverse_lazy is used to reverse the url

    #what to do with the form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


    