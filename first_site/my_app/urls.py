from django.urls import path
from . import views

#my_domain.com/my_app/simple_view
urlpatterns = [
    path('<int:num_page>/',views.num_page_view),
    path('<str:topic>/',views.news_view,name='topic'),
    path('<int:num1>/<int:num2>',views.add_view),
    path('',views.simple_view)

]

