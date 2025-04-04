from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

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
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404()

def add_view(request, num1, num2):
    #domain.com/my_app/num1/num2
    result = num1 + num2
    return HttpResponse(str(result))

def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    webpage = reverse('topic',args=[topic])

    return HttpResponseRedirect(webpage)

def simple_view(request):
    return render(request, 'my_app/example.html' )