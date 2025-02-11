from django.shortcuts import render, redirect
from django.urls import reverse 
from . import models
from .forms import ReviewForm

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    return render(request, 'cars/list.html', context={'all_cars': all_cars})

def add(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = int(request.POST.get('year'))
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))

    return render(request, 'cars/add.html')

def delete(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        try:
            car = models.Car.objects.get(pk=pk)
            car.delete()
        except:
            print('Car not found')
        return redirect(reverse('cars:list'))
    return render(request, 'cars/delete.html')

def rental_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()
        return render(request, 'cars/rental_review.html', context={'form': form})

def thank_you(request):
    return render(request, 'cars/thank_you.html')