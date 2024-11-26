from django.urls import path
from . import views

#my_domain.com/my_app/simple_view
urlpatterns = [
    path("", views.index,name='index'),   #/my_app => Project urls.py
    path("simple_view", views.simple_view),

]

