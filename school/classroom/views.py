from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    fields = "__all__"
    model = Teacher
    # it will look for 'classroom/teacher_form.html'
    success_url = reverse_lazy('classroom:thank_you')

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

class TeacherListView(ListView):
    # it will look for 'classroom/teacher_list.html'
    model = Teacher
    context_object_name = 'teachers'  #default is 'object_list'
    queryset = Teacher.objects.filter(subject='Box') #default is Teacher.objects.all() 

class TeacherDetailView(DetailView):
    model = Teacher
    # look for 'classroom/teacher_detail.html'

class TeacherUpdateView(UpdateView):
    model = Teacher
    # shares the same template as CreateView

    # for custom template:
    fields = ['last_name', 'subject']
    success_url = reverse_lazy('classroom:list_teachers')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:list_teachers')
    # look for 'classroom/teacher_confirm_delete.html'