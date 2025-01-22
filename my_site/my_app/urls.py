from django.urls import path
from . import views

# register the app namespace, so Django can distinguish between different apps for URL NAMES
app_name = "my_app"

urlpatterns = [
    path("", views.example_view, name="example"),
    path("variable/", views.variable_view, name="variable"),
]