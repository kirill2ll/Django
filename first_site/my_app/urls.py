from django.urls import path
from . import views

#my_domain.com/my_app/simple_view
urlpatterns = [
    path('<str:topic>/',views.news_view),
    path('<int:num1>/<int:num2>',views.add_view),

]

