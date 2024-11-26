from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports': 'Sport Page',
    'finance': 'Finace Page',
    'politics': 'Politics Page',
}

# def sports_view(request):
#     return HttpResponse(articles['sports'])

# def finance_view(request):
#     return HttpResponse(articles['finance'])

def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    #domain.com/my_app/num1/num2
    result = num1 + num2
    return HttpResponse(str(result))